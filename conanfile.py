from conans import ConanFile, tools

class GslliteConan(ConanFile):
    name = "gsl-lite"
    version = "0.25.0"
    license = "MIT"
    url = "https://github.com/martinmoene/gsl-lite"
    description = "A single-file header-only version of ISO C++ Guideline Support Library (GSL) for C++98, C++11 and later"

    def source(self):
        self.run("git clone https://github.com/martinmoene/gsl-lite.git")
        self.run("cd gsl-lite && git checkout v0.25.0")

    def package(self):
        self.copy(pattern="gsl-lite.h", src="gsl-lite/include/gsl", dst="include", keep_path=False)
