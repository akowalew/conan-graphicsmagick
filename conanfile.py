from conans import ConanFile, tools, AutoToolsBuildEnvironment

class GraphicsmagickConan(ConanFile):
    name = "graphicsmagick"
    version = "1.3.28"
    license = "MIT"
    author = "Adam Kowalewski ram.techen@gmail.com"
    url = "https://github.com/akowalew/conan-graphicsmagick/issues"
    description = "GraphicsMagick is the swiss army knife of image processing"
    topics = ("graphics", "media")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        tools.download("https://sourceforge.net/projects/graphicsmagick/files/graphicsmagick/1.3.28/GraphicsMagick-1.3.28.tar.gz", "GraphicsMagick-1.3.28.tar.gz")
        tools.untargz("GraphicsMagick-1.3.28.tar.gz")

    def build(self):
        args = [
            "--with-quantum-depth=16",
            "--enable-shared=yes",
            "--enable-static=no",
            "--without-bzlib",
            "--without-dps",
            "--without-fpx",
            "--without-gslib",
            "--without-jbig",
            "--without-jpeg",
            "--without-jp2",
            "--without-lcms2",
            "--without-lzma",
            "--without-magick-plus-plus",
            "--without-png",
            "--without-tiff",
            "--without-trio",
            "--without-ttf",
            "--without-umem",
            "--without-wmf",
            "--without-webp",
            "--without-x",
            "--without-xml",
            "--without-zlib",
        ]
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir="GraphicsMagick-1.3.28", args=args)
        autotools.make()
        autotools.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.includedirs = ['include/GraphicsMagick']
        self.cpp_info.libs = ["GraphicsMagick"]

