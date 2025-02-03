"""Static site generation using Frozen-Flask."""

import sys
from pathlib import Path

# Add project root to sys.path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))  # Ensure src/ is at the start of sys.path

from flask_frozen import Freezer
from app import create_app

# Create Flask app with production configuration
app = create_app("production")

# Set the build directory outside of src/
app.config["FREEZER_DESTINATION"] = str(project_root.parent / "docs")

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
