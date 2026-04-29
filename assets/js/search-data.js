// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-teaching",
          title: "teaching",
          description: "Classes I have officially tutored or TA&#39;d for",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "post-independence-of-irrelevant-alternatives",
        
          title: "Independence of Irrelevant Alternatives",
        
        description: "A brief exploration of the Independence of Irrelevant Alternatives (IIA) condition in voting systems, and why its absence makes voting systems behave irrationally.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/iia/";
          
        },
      },{id: "post-is-the-condorcet-winner-the-true-compromise",
        
          title: "Is the Condorcet Winner the True Compromise?",
        
        description: "A Condorcet winner may not be a true consensus candidate. Approval voting can find consensus with a simpler ballot.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/why-condorcet/";
          
        },
      },{id: "post-why-i-currently-only-support-approval",
        
          title: "Why I Currently Only Support Approval",
        
        description: "Why Approval voting is the only system I trust to push for right now.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/approval-only/";
          
        },
      },{id: "post-approval-is-the-perfect-condorcet-method",
        
          title: "Approval is the Perfect Condorcet Method",
        
        description: "Approval is a perfect Condorcet method, and I have permanently solved the Condorcet paradox. April Fools!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/condorcet-approval/";
          
        },
      },{id: "post-the-gibbard-satterthwaite-theorem",
        
          title: "The Gibbard-Satterthwaite Theorem",
        
        description: "A walkthrough and proof of the theorem that proves ranked voting systems must be susceptible to strategic voting.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/gibbard-satt/";
          
        },
      },{id: "post-it-39-s-time-to-ditch-rcv-embrace-approval-voting",
        
          title: "It&#39;s Time to Ditch RCV, Embrace Approval Voting",
        
        description: "It has been tried, and it has failed. Ranked-choice voting must go before it poisons the well for all electoral reform.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/ditch-rcv/";
          
        },
      },{id: "post-approval-voting-is-the-only-internally-consistent-cardinal-method",
        
          title: "Approval voting is the Only Internally Consistent Cardinal Method",
        
        description: "A proof that Approval voting is the unique score aggregation voting method that satisfies Score-Condorcet-Consistency, an arguably necessary property for a trustworthy voting system.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/consistentcardinal/";
          
        },
      },{id: "post-a-practical-case-for-approval-voting",
        
          title: "A Practical Case for Approval Voting",
        
        description: "It&#39;s not just mathematically elegant, it&#39;s the most practical solution for our electoral problems.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/practicalapproval/";
          
        },
      },{id: "post-the-lichtman-perception-paradox",
        
          title: "The Lichtman Perception Paradox",
        
        description: "A mathematician&#39;s take on Allan Lichtman&#39;s keys to the White House.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/lichtman/";
          
        },
      },{id: "post-is-approval-voting-strategyproof",
        
          title: "Is Approval Voting Strategyproof?",
        
        description: "Well yes, but actually no. Unless...",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/avstratproof/";
          
        },
      },{id: "post-a-mathematical-case-for-approval-voting",
        
          title: "A Mathematical Case for Approval Voting",
        
        description: "Approval voting is the best voting system (AKA, Taylor gets political). (Somewhat outdated.)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/approval/";
          
        },
      },{id: "post-why-do-we-row-reduce-what-is-a-matrix",
        
          title: "Why do we row reduce? What IS a matrix?",
        
        description: "What does the RREF tell us, and why do we spend so much time on it? Why do we define matrix multiplication the way we do?",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/rref/";
          
        },
      },{id: "post-introduction-to-least-squares-part-2-electric-boogaloo",
        
          title: "Introduction to Least Squares Part 2 (Electric Boogaloo)",
        
        description: "Why the heck do we multiply by the transpose",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/leastsquarespart2/";
          
        },
      },{id: "post-the-wonderful-world-of-projectors",
        
          title: "The Wonderful World of Projectors",
        
        description: "They&#39;re cool, I promise!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/projectors/";
          
        },
      },{id: "post-constant-coefficient-odes-made-simple-with-linear-operators",
        
          title: "Constant Coefficient ODEs Made Simple with Linear Operators",
        
        description: "No more guessing. Let&#39;s make it intuitive with linear algebra.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/linalglinconstcoef/";
          
        },
      },{id: "post-in-defense-of-cramer-39-s-rule",
        
          title: "In Defense of Cramer&#39;s Rule",
        
        description: "(and determinants)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/cramers/";
          
        },
      },{id: "post-change-of-basis",
        
          title: "Change of Basis",
        
        description: "the most confusing thing in linear algebra (don&#39;t @ me)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/changeofbasis/";
          
        },
      },{id: "post-linear-constant-coefficient-odes",
        
          title: "Linear Constant Coefficient ODEs",
        
        description: "the most important topic in an ODE class",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/linconstcoef/";
          
        },
      },{id: "post-integrating-factors-explained",
        
          title: "Integrating Factors Explained",
        
        description: "the most common way to solve first order linear ODE&#39;s",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/integratingfactor/";
          
        },
      },{id: "post-bases-for-the-fundamental-spaces-of-a-matrix",
        
          title: "Bases for the fundamental spaces of a matrix",
        
        description: "a lot of students struggle with this so here. row space, column space, null space, and left null space.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/rowcolspace/";
          
        },
      },{id: "post-series-solutions-done-quick",
        
          title: "Series Solutions Done Quick",
        
        description: "the fast way to do series solutions. no reindexing required.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/seriessolutions/";
          
        },
      },{id: "post-column-and-row-perspective",
        
          title: "Column and Row Perspective",
        
        description: "How to simplify matrix multiplication with the best perspectives (and also find certain inverse matrices fast!)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/columnperspective/";
          
        },
      },{id: "post-new-ways-to-calculate-normalized-solutions-to-linear-constant-coefficient-differential-equations",
        
          title: "New Ways to Calculate Normalized Solutions to Linear Constant-Coefficient Differential Equations",
        
        description: "The fastest way for a computer, and a fast way by hand.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/newnormalized/";
          
        },
      },{id: "post-systems-of-linear-difference-equations",
        
          title: "Systems of Linear Difference Equations",
        
        description: "Like systems of ODEs, but discrete 👀",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/discretesystems/";
          
        },
      },{id: "post-matrix-exponential-formulas-for-2x2-matrices",
        
          title: "Matrix Exponential Formulas for 2x2 Matrices",
        
        description: "Who needs eigenvectors?",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2x2ezmatrixexp/";
          
        },
      },{id: "post-2x2-matrix-exponential-formulas-with-differential-equations",
        
          title: "2x2 Matrix Exponential Formulas with Differential Equations",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2x2matrixexpwde/";
          
        },
      },{id: "post-solving-systems-of-first-order-odes-like-a-baller",
        
          title: "Solving systems of first-order ODEs like a baller",
        
        description: "some ballin&#39; tips and tricks",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/firstordersystemsquick/";
          
        },
      },{id: "post-shortcuts-for-finding-eigenvalues-and-eigenvectors",
        
          title: "Shortcuts for Finding Eigenvalues and Eigenvectors",
        
        description: "diagonalization speedrun, let&#39;s go",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/eigentricks/";
          
        },
      },{id: "post-easily-solving-autonomous-ivps-off-the-origin",
        
          title: "Easily Solving Autonomous IVPs Off the Origin",
        
        description: "Easily solving linear homogeneous constant coefficient initial problems when the initial point is not t=0",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/autonomousivps/";
          
        },
      },{id: "post-introduction-to-least-squares",
        
          title: "Introduction to Least Squares",
        
        description: "How to find the best solution for an inconsistent system",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/leastsquares/";
          
        },
      },{id: "post-finding-taylor-series-of-polynomials-using-synthetic-division",
        
          title: "Finding Taylor Series of Polynomials Using Synthetic Division",
        
        description: "Wait you can do that? YUP",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/synthetictaylor/";
          
        },
      },{id: "post-a-formula-for-some-particular-solutions",
        
          title: "A Formula for Some Particular Solutions",
        
        description: "Yet another obnoxious formula for solutions to constant coefficient nonhomogeneous ODE&#39;s with common forcing functions.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/exppolynonhomo/";
          
        },
      },{id: "post-matrix-exponentials-using-differential-equations",
        
          title: "Matrix Exponentials Using Differential Equations",
        
        description: "ok",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/matrixexpwde/";
          
        },
      },{id: "post-exact-equations-done-quick",
        
          title: "Exact Equations Done Quick",
        
        description: "speedrun WR",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/exacteqs/";
          
        },
      },{id: "post-function-interpolation",
        
          title: "Function Interpolation",
        
        description: "Find a function that matches your requirements",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/functioninterp/";
          
        },
      },{id: "post-polynomial-interpolation",
        
          title: "Polynomial Interpolation",
        
        description: "Making your own custom polynomial.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/polyinterp/";
          
        },
      },{id: "post-intro-to-solving-systems-of-first-order-differential-equations",
        
          title: "Intro To Solving Systems of First Order Differential Equations",
        
        description: "An attempt at an intuitive derivation",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/firstordersystemsolve/";
          
        },
      },{id: "post-variation-of-parameters-using-linear-algebra",
        
          title: "Variation of Parameters Using Linear Algebra",
        
        description: "linear is best frend :)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/voplinear/";
          
        },
      },{id: "post-solving-second-order-systems-of-differential-equations",
        
          title: "Solving Second Order Systems of Differential Equations",
        
        description: "ye",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2ndordersystemsolve/";
          
        },
      },{id: "post-tricks-for-remembering-laplace-transforms",
        
          title: "Tricks for Remembering Laplace Transforms",
        
        description: "for students and people who forgot",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/laplacetricks/";
          
        },
      },{id: "post-skipping-integration-by-parts-using-euler-39-s-formula",
        
          title: "Skipping Integration by Parts Using Euler&#39;s Formula",
        
        description: "skip or simplify integrals involving trig functions multiplied by exponentials",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/eulersformulabyparts/";
          
        },
      },{id: "post-introduction-to-euler-39-s-formula",
        
          title: "Introduction to Euler&#39;s Formula",
        
        description: "the best formula",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/eulersformula/";
          
        },
      },{id: "post-constructing-integer-2x2-second-order-systems-of-differential-equations-with-integer-solutions",
        
          title: "Constructing Integer 2x2 Second Order Systems of Differential Equations with Integer Solutions",
        
        description: "It&#39;s a lot messier.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/secondordersystems/";
          
        },
      },{id: "post-constructing-integer-2x2-first-order-systems-of-differential-equations-with-integer-solutions",
        
          title: "Constructing Integer 2x2 First Order Systems of Differential Equations with Integer Solutions",
        
        description: "Nice solutions? Nice.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/firstordersystems/";
          
        },
      },{id: "post-matrix-exponential-formulas-for-2x2-matrices-using-laplace-transforms",
        
          title: "Matrix Exponential Formulas for 2x2 Matrices Using Laplace Transforms",
        
        description: "this has been rewritten",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/ezmatrixexp/";
          
        },
      },{id: "post-eigendecomposition-of-real-matrices-with-complex-eigenvalues",
        
          title: "Eigendecomposition of Real Matrices with Complex Eigenvalues",
        
        description: "An attempt at an intuitive derivation.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/complexeigenvalues/";
          
        },
      },{id: "post-solving-multiple-initial-value-problems-with-normalized-solutions",
        
          title: "Solving Multiple Initial Value Problems with Normalized Solutions",
        
        description: "Solve one, solve them all.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/normalized/";
          
        },
      },{id: "post-constructing-2x2-markov-matrices",
        
          title: "Constructing 2x2 Markov Matrices",
        
        description: "Build a Markov Chain with desired behavior.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/markovbuild/";
          
        },
      },{id: "post-linear-differential-equation-interpolation",
        
          title: "Linear Differential Equation Interpolation",
        
        description: "Linear Differential Equations with desired solutions using determinants.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/diffeqinterp/";
          
        },
      },{id: "post-skew-symmetric-matrices-are-cool",
        
          title: "Skew-Symmetric Matrices Are Cool",
        
        description: "top 10 things YOU didn&#39;t know about real skew-symmetric matrices!!! (GONE WRONG) (COPS CALLED)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/skewsymmetric/";
          
        },
      },{id: "post-the-alpha-method-generalized-exponential-response-formula",
        
          title: "The Alpha Method (Generalized Exponential Response Formula)",
        
        description: "Easy particular solutions to nonhomoegenous constant coefficient linear differential equations with simple exponential/trigonometric forcing functions.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/alphamethod/";
          
        },
      },{id: "post-implicit-solutions-to-2x2-systems-of-first-order-homogeneous-linear-differential-equations",
        
          title: "Implicit Solutions to 2x2 Systems of First-Order Homogeneous Linear Differential Equations",
        
        description: "Implicit and explicit solutions for all cases.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2x2implicit/";
          
        },
      },{id: "post-exponentials-of-symmetric-matrices-using-the-spectral-theorem",
        
          title: "Exponentials of Symmetric Matrices Using the Spectral Theorem",
        
        description: "yeah",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/symmetric-exp/";
          
        },
      },{id: "post-constructing-systems-of-nonlinear-first-order-differential-equations-to-model-population-dynamics",
        
          title: "Constructing Systems of Nonlinear First-Order Differential Equations to Model Population Dynamics",
        
        description: "Build a system with desired behavior.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/nonlinearbuild/";
          
        },
      },{id: "post-a-different-perspective-of-diagonalization",
        
          title: "A Different Perspective of Diagonalization",
        
        description: "An (atttempt at an) intuitive approach to similar matrix decomposition.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/diagonalization/";
          
        },
      },{id: "news-a-simple-inline-announcement",
          title: 'A simple inline announcement.',
          description: "",
          section: "News",},{id: "news-a-long-announcement-with-details",
          title: 'A long announcement with details',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_2/";
            },},{id: "news-a-simple-inline-announcement-with-markdown-emoji-sparkles-smile",
          title: 'A simple inline announcement with Markdown emoji! :sparkles: :smile:',
          description: "",
          section: "News",},{id: "news-new-news-now-upside-down-face",
          title: 'new news now :upside_down_face:',
          description: "",
          section: "News",},{id: "news-updating-posts-to-the-distill-theme",
          title: 'updating posts to the distill theme',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/distill1/";
            },},{id: "news-2x2-matrix-exponentials-post-rewritten",
          title: '2x2 matrix exponentials post rewritten',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/updateezmatrix/";
            },},{id: "news-back-with-a-few-new-posts",
          title: 'back with a few new posts',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/backin2022/";
            },},{id: "previews-a-mathematical-case-for-approval-voting",
          title: 'A Mathematical Case for Approval Voting',
          description: "Approval voting is the best voting system (AKA, Taylor gets political)",
          section: "Previews",handler: () => {
              window.location.href = "/preview/approval/";
            },},{id: "previews-irv-inconsistencies",
          title: 'IRV Inconsistencies',
          description: "It&#39;s much worse than you think.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/not-irv/";
            },},{id: "previews-a-practical-case-for-approval-voting",
          title: 'A Practical Case for Approval Voting',
          description: "It&#39;s not just mathematically elegant, it&#39;s the most practical solution for our electoral problems.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/practicalapproval/";
            },},{id: "previews-deducing-possible-approval-outcomes-from-ranked-ballots",
          title: 'Deducing Possible Approval Outcomes from Ranked Ballots',
          description: "A theoretical and practical exploration of cutting through the inherent indeterminacy of approval voting using ranked ballots. Exploring AK 2022 and a notable Minnesota election.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/ranked-to-av/";
            },},{id: "previews-the-gibbard-satterthwaite-theorem",
          title: 'The Gibbard-Satterthwaite Theorem',
          description: "A walkthrough and proof of the theorem that proves ranked voting systems must be susceptible to strategic voting.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/gibbard-satt/";
            },},{id: "previews-the-approval-dynamics-of-laslier-39-s-leader-rule",
          title: 'The Approval Dynamics of Laslier&amp;#39;s Leader Rule',
          description: "How the leader rule induces a graph and dynamical system on candidate perceptions.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/leader-dynamics/";
            },},{id: "previews-approval-is-a-condorcet-method",
          title: 'Approval is a Condorcet Method',
          description: "Approval is the perfect Condorcet method, and I have permanently solved the Condorcet paradox. April Fools!",
          section: "Previews",handler: () => {
              window.location.href = "/preview/condorcetapproval/";
            },},{id: "previews-approval-is-the-perfect-condorcet-method",
          title: 'Approval is the Perfect Condorcet Method',
          description: "Approval is a perfect Condorcet method, and I have permanently solved the Condorcet paradox. April Fools!",
          section: "Previews",handler: () => {
              window.location.href = "/preview/condorcet-approval/";
            },},{id: "previews-a-guide-to-approval-voting-strategy",
          title: 'A Guide to Approval Voting Strategy',
          description: "An explanation of the leader rule strategy in approval voting, and its positive ramifications.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/avstrategy/";
            },},{id: "previews-arrow-39-s-impossibility-theorem",
          title: 'Arrow&amp;#39;s Impossibility Theorem',
          description: "Walkthrough and proof of the theorem that proves ranked voting systems cannot satisfy seemingly reasonable properties.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/arrows-old/";
            },},{id: "previews-why-i-currently-only-support-approval",
          title: 'Why I Currently Only Support Approval',
          description: "Approval voting is the only system I trust to push for right now, and here&#39;s why.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/approval-only/";
            },},{id: "previews-is-the-condorcet-winner-the-true-compromise",
          title: 'Is the Condorcet Winner the True Compromise?',
          description: "A Condorcet winner may not be a true consensus candidate. Approval voting can find consensus with a simpler ballot.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/why-condorcet/";
            },},{id: "previews-the-perfection-of-approval-voting",
          title: 'The Perfection of Approval Voting',
          description: "A mathematical dive into the fundamental nature of Approval voting on dichotomous preferences.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/perfect-approval/";
            },},{id: "previews-arrow-39-s-impossibility-theorem",
          title: 'Arrow&amp;#39;s Impossibility Theorem',
          description: "Walkthrough and proof of the theorem that proves ranked voting systems cannot satisfy seemingly reasonable properties.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/arrows/";
            },},{id: "previews-independence-of-irrelevant-alternatives",
          title: 'Independence of Irrelevant Alternatives',
          description: "A brief exploration of the Independence of Irrelevant Alternatives (IIA) condition in voting systems, and why its absence makes voting systems behave irrationally.",
          section: "Previews",handler: () => {
              window.location.href = "/preview/iia/";
            },},{id: "previews-jordan-canonical-form-made-easier-part-1",
          title: 'Jordan Canonical Form Made Easier Part 1',
          description: "not easy. just like... easier...",
          section: "Previews",handler: () => {
              window.location.href = "/preview/jordan/";
            },},{id: "previews-jordan-canonical-form-made-easier",
          title: 'Jordan Canonical Form Made Easier',
          description: "not easy. just like... easier...",
          section: "Previews",handler: () => {
              window.location.href = "/preview/jordan2/";
            },},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-project-6",
          title: 'project 6',
          description: "a project with no image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{id: "projects-just-how-chaotic-is-the-electoral-college",
          title: 'Just how chaotic is the electoral college?',
          description: "An analysis of how close US elections really are",
          section: "Projects",handler: () => {
              window.location.href = "/projects/EC_margins/";
            },},{id: "projects-title",
          title: 'Title',
          description: "desc",
          section: "Projects",handler: () => {
              window.location.href = "/projects/template/";
            },},{
        id: 'social-discord',
        title: 'Discord',
        section: 'Socials',
        handler: () => {
          window.open("https://discord.com/users/196803594576592896", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%74%61%79%6C%6F%72%65%69%67%65%6E%66%69%73%68%65%72@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/eigentaylor", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
