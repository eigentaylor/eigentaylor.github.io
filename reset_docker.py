#!/usr/bin/env python3
"""
Docker Reset Script for al-folio Development
This script stops, removes, and restarts the Docker container for local development.
"""

import subprocess
import sys
import time
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        # Run command without capturing output for real-time feedback
        result = subprocess.run(command, shell=True, cwd=os.getcwd())
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
        else:
            print(f"❌ {description} failed (exit code: {result.returncode})")
            return False
        return True
    except Exception as e:
        print(f"❌ Error running {description}: {e}")
        return False

def run_command_with_output(command, description):
    """Run a command and capture output"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            if result.stdout.strip():
                print(result.stdout.strip())
        else:
            print(f"❌ {description} failed")
            if result.stderr.strip():
                print(f"   Error: {result.stderr.strip()}")
            return False
        return True
    except Exception as e:
        print(f"❌ Error running {description}: {e}")
        return False

def main():
    print("🐳 al-folio Docker Reset Script")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("docker-compose.yml"):
        print("❌ Error: docker-compose.yml not found!")
        print("   Make sure you're running this script from the al-folio project directory.")
        sys.exit(1)
    
    print("📍 Current directory:", os.getcwd())
    
    # Stop and remove containers
    print("\n� Stopping any running containers...")
    run_command("docker compose down", "Stopping Docker containers")
    
    # Pull latest images
    print("\n📦 Pulling latest images...")
    if not run_command("docker compose pull", "Pulling latest Docker images"):
        print("❌ Failed to pull Docker images. Exiting.")
        sys.exit(1)
    
    # Start containers
    print("\n🚀 Starting containers...")
    if not run_command("docker compose up -d", "Starting containers in background"):
        print("❌ Failed to start containers. Exiting.")
        sys.exit(1)
    
    # Wait a moment for container to start
    print("\n⏳ Waiting for container to initialize...")
    for i in range(10):
        print(f"   {i+1}/10 seconds...", end='\r')
        time.sleep(1)
    print()
    
    # Check container status
    print("\n📊 Checking container status...")
    run_command_with_output("docker compose ps", "Container status")
    
    # Show logs
    print("\n📋 Recent container logs:")
    run_command_with_output("docker compose logs --tail=20", "Showing recent logs")
    
    print("\n" + "=" * 40)
    print("🎉 Docker reset complete!")
    print("🌐 Your site should be available at: http://localhost:8080")
    print("📝 To view live logs: docker compose logs -f")
    print("🛑 To stop containers: docker compose down")
    print("\n💡 If the site isn't loading, try waiting 30-60 seconds for Jekyll to build.")

if __name__ == "__main__":
    main()
