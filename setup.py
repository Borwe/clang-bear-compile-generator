#/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()
	
	setuptools.setup(
		name="clang_bear_compiler", 
		version="0.0.1",
		author="Brian Orwe",
		description="simple program to generate compile_commands.json for clang(d)",
		long_description=long_description,
		long_description_content_type="text/markdown",
		url="https://github.com/Borwe/clang-bear-compile-generator",
		packages=setuptools.find_packages(),
		classifiers=[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			],
		python_requires='>=3.6',
	)
