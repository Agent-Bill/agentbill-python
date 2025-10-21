from setuptools import setup, find_packages
import sys

if len(sys.argv) == 1:
    print("\nPlease specify a setup.py command. Common commands are:")
    print("  install       : Install the package in the current Python environment")
    print("  develop      : Install the package in development/editable mode")
    print("  sdist        : Create a source distribution package")
    print("  bdist_wheel  : Create a wheel distribution package")
    print("\nExample usage:")
    print("  python setup.py install")
    print("  python setup.py develop")
    print("\nFor a complete list of commands, use:")
    print("  python setup.py --help-commands\n")
    sys.exit(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agentbill",
    version="1.0.0",
    author="AgentBill",
    author_email="support@agentbill.com",
    description="OpenTelemetry-based SDK for tracking AI agent usage and billing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Agent-Bill/python",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "httpx>=0.24.0",
    ],
    extras_require={
        "openai": ["openai>=1.0.0"],
        "anthropic": ["anthropic>=0.9.0"],
    },
    keywords="opentelemetry otel ai agent billing usage-tracking openai anthropic llm observability",
)
