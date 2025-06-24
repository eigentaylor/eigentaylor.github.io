#!/usr/bin/env python3
"""
Simple Docker Reset Script for al-folio
Just runs the basic commands to restart Docker
"""

import subprocess
import os

def run_cmd(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    print("Resetting Docker...")
    
    # Basic commands
    run_cmd("docker compose down")
    run_cmd("docker compose pull")
    run_cmd("docker compose up -d")
    
    print("Done! Check http://localhost:8080")
