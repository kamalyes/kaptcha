import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kaptcha",
    version="1.0.1",
    author="kamalyes",
    description="一个图形验证码生成工具",
    author_email="mryu168@163.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamalyes/kaptcha",
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pillow"],
    keywords="Captcha Verification-Code Code",
    include_package_data=True,
    python_requires=">3.7"
)
