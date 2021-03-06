workspace(name = "distroless")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_file")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "new_git_repository")

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "8df59f11fb697743cbb3f26cfb8750395f30471e9eabde0d174c3aebc7a1cd39",
    urls = [
        "https://storage.googleapis.com/bazel-mirror/github.com/bazelbuild/rules_go/releases/download/0.19.1/rules_go-0.19.1.tar.gz",
        "https://github.com/bazelbuild/rules_go/releases/download/0.19.1/rules_go-0.19.1.tar.gz",
    ],
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.0.1/rules_python-0.0.1.tar.gz",
    sha256 = "aa96a691d3a8177f3215b14b0edc9641787abaaa30363a080165d06ab65e1161",
)
load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()
# Only needed if using the packaging rules.
load("@rules_python//python:pip.bzl", "pip_repositories")
pip_repositories()

go_rules_dependencies()

go_register_toolchains()

load("//package_manager:package_manager.bzl", "package_manager_repositories")
load("//package_manager:dpkg.bzl", "dpkg_list", "dpkg_src")

package_manager_repositories()

dpkg_src(
    name = "debian_stretch",
    arch = "amd64",
    distro = "stretch",
    sha256 = "2b13362808b7bd90d24db2e0804c799288694ae44bd7e3d123becc191451fc67",
    snapshot = "20191028T085816Z",
    url = "https://snapshot.debian.org/archive",
)

dpkg_src(
    name = "debian_stretch_backports",
    arch = "amd64",
    distro = "stretch-backports",
    sha256 = "e9170a8f37a1bbb8ce2df49e6ab557d65ef809d19bf607fd91bcf8ba6b85e3f6",
    snapshot = "20191028T085816Z",
    url = "https://snapshot.debian.org/archive",
)

dpkg_src(
    name = "debian_stretch_security",
    package_prefix = "https://snapshot.debian.org/archive/debian-security/20191028T085816Z/",
    packages_gz_url = "https://snapshot.debian.org/archive/debian-security/20191028T085816Z/dists/stretch/updates/main/binary-amd64/Packages.gz",
    sha256 = "acea7d952d8ab84de3cd2c26934a1bcf5ad244d344ecdb7b2d0173712bbd9d7b",
)

dpkg_list(
    name = "package_bundle",
    packages = [
        # Version required to skip a security fix to the pre-release library
        # TODO: Remove when there is a security fix or dpkg_list finds the recent version
        "libc6=2.24-11+deb9u4",
        "base-files",
        "ca-certificates",
        "openssl",
        "libssl1.0.2",
        "libssl1.1",
        "libbz2-1.0",
        "libdb5.3",
        "libffi6",
        "libncursesw5",
        "liblzma5",
        "libexpat1",
        "libreadline7",
        "libtinfo5",
        "libsqlite3-0",
        "mime-support",
        "netbase",
        "readline-common",
        "tzdata",

        #c++
        "libgcc1",
        "libgomp1",
        "libstdc++6",

        #java
        "zlib1g",
        "libjpeg62-turbo",
        "libpng16-16",
        "liblcms2-2",
        "libfreetype6",
        "fonts-dejavu-core",
        "fontconfig-config",
        "libfontconfig1",
        "openjdk-8-jre-headless",
        "openjdk-11-jre-headless",

        #python
        "libpython2.7-minimal",
        "python2.7-minimal",
        "libpython2.7-stdlib",
        "dash",
        # Version required to skip a security fix to the pre-release library
        # TODO: Remove when there is a security fix or dpkg_list finds the recent version
        "libc-bin=2.24-11+deb9u4",
	"python-bitarray",
	"python-pkg-resources",
	"python-setuptools",
	"python-crypto",

        #python3
        "libmpdec2",
        "libpython3.5-minimal",
        "libpython3.5-stdlib",
        "python3.5-minimal",

        #dotnet
        "libcurl3",
        "libgssapi-krb5-2",
        "libicu57",
        "liblttng-ust0",
        "libssl1.0.2",
        "libunwind8",
        "libuuid1",
        "zlib1g",
        "curl",
        "libcomerr2",
        "libidn2-0",
        "libk5crypto3",
        "libkrb5-3",
        "libldap-2.4-2",
        "libldap-common",
        "libsasl2-2",
        "libnghttp2-14",
        "libpsl5",
        "librtmp1",
        "libssh2-1",
        "libkeyutils1",
        "libkrb5support0",
        "libunistring0",
        "libgnutls30",
        "libgmp10",
        "libhogweed4",
        "libidn11",
        "libnettle6",
        "libp11-kit0",
        "libffi6",
        "libtasn1-6",
        "libsasl2-modules-db",
        "libgcrypt20",
        "libgpg-error0",
        "libacl1",
        "libattr1",
        "libselinux1",
        "libpcre3",
        "libbz2-1.0",
        "liblzma5",
    ],
    # Takes the first package found: security updates should go first
    # If there was a security fix to a package before the stable release, this will find
    # the older security release. This happened for stretch libc6.
    sources = [
        "@debian_stretch_security//file:Packages.json",
        "@debian_stretch_backports//file:Packages.json",
        "@debian_stretch//file:Packages.json",
    ],
)

# For Jetty
http_archive(
    name = "jetty",
    build_file = "//:BUILD.jetty",
    sha256 = "1b9ec532cd9b94550fad655e066a1f9cc2d350a1c79daea85d5c56fdbcd9aaa8",
    strip_prefix = "jetty-distribution-9.4.22.v20191022/",
    type = "tar.gz",
    urls = ["https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/9.4.22.v20191022/jetty-distribution-9.4.22.v20191022.tar.gz"],
)

# Node
http_archive(
    name = "nodejs",
    build_file = "//experimental/nodejs:BUILD.nodejs",
    sha256 = "417bdc5402f6510fe1a5a898a9cdf1d67bd0202b5f014051c382f05358999534",
    strip_prefix = "node-v10.17.0-linux-x64/",
    type = "tar.gz",
    urls = ["https://nodejs.org/dist/v10.17.0/node-v10.17.0-linux-x64.tar.gz"],
)

# dotnet
http_archive(
    name = "dotnet",
    build_file = "//experimental/dotnet:BUILD.dotnet",
    sha256 = "69ecad24bce4f2132e0db616b49e2c35487d13e3c379dabc3ec860662467b714",
    type = "tar.gz",
    urls = ["https://download.microsoft.com/download/5/F/0/5F0362BD-7D0A-4A9D-9BF9-022C6B15B04D/dotnet-runtime-2.0.0-linux-x64.tar.gz"],
)

# For the debug image
http_file(
    name = "busybox",
    executable = True,
    sha256 = "b51b9328eb4e60748912e1c1867954a5cf7e9d5294781cae59ce225ed110523c",
    urls = ["https://busybox.net/downloads/binaries/1.27.1-i686/busybox"],
)

# Docker rules.
http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "413bb1ec0895a8d3249a01edf24b82fd06af3c8633c9fb833a0cb1d4b234d46d",
    strip_prefix = "rules_docker-0.12.0",
    urls = ["https://github.com/bazelbuild/rules_docker/archive/v0.12.0.tar.gz"],
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)

container_repositories()

load("@io_bazel_rules_docker//container:container.bzl", "container_pull")

# Used to generate java ca certs.
container_pull(
    name = "debian9",
    # From tag: 2019-02-27-130449
    digest = "sha256:fd26dfa474b76ef931e439537daba90bbd90d6c5bbdd0252616e6d87251cd9cd",
    registry = "gcr.io",
    repository = "google-appengine/debian9",
)

# Have the py_image dependencies for testing.
load(
    "@io_bazel_rules_docker//python:image.bzl",
    _py_image_repos = "repositories",
)

_py_image_repos()

# Have the java_image dependencies for testing.
load(
    "@io_bazel_rules_docker//java:image.bzl",
    _java_image_repos = "repositories",
)

_java_image_repos()

# Have the go_image dependencies for testing.
load(
    "@io_bazel_rules_docker//go:image.bzl",
    _go_image_repos = "repositories",
)

_go_image_repos()

dpkg_src(
    name = "debian10",
    arch = "amd64",
    distro = "buster",
    sha256 = "ca19e4187523f4b087a2e7aaa2662c6a0b46dc81ff2f3dd44d9c5d95df0df212",
    snapshot = "20191028T085816Z",
    url = "https://snapshot.debian.org/archive",
)

dpkg_list(
    name = "package_bundle_debian10",
    packages = [
        "libc6",
        "base-files",
        "ca-certificates",
        "openssl",
        "libssl1.1",
        "libbz2-1.0",
        "libdb5.3",
        "libffi6",
        "liblzma5",
        "libexpat1",
        "libreadline7",
        "libsqlite3-0",
        "mime-support",
        "netbase",
        "readline-common",
        "tzdata",

        #c++
        "libgcc1",
        "libgomp1",
        "libstdc++6",

        #java
        "zlib1g",
        "libjpeg62-turbo",
        "libpng16-16",
        "liblcms2-2",
        "libfreetype6",
        "fonts-dejavu-core",
        "fontconfig-config",
        "libfontconfig1",
        "openjdk-11-jre-headless",

        #python
        "dash",
        "libc-bin",
        "libpython2.7-minimal",
        "libpython2.7-stdlib",
        "python2.7-minimal",
	"python-bitarray",
	"python-pkg-resources",
	"python-setuptools",
	"python-crypto",

        #python3
        "libmpdec2",
        "libpython3.7-minimal",
        "libpython3.7-stdlib",
        "libtinfo6",
        "libuuid1",
        "libncursesw6",
        "python3.7-minimal",

    ],
    # Takes the first package found: security updates should go first
    # If there was a security fix to a package before the stable release, this will find
    # the older security release. This happened for stretch libc6.
    sources = [
        "@debian10_security//file:Packages.json",
        "@debian10//file:Packages.json",
    ],
)

dpkg_src(
    name = "debian10_security",
    package_prefix = "https://snapshot.debian.org/archive/debian-security/20191028T085816Z/",
    packages_gz_url = "https://snapshot.debian.org/archive/debian-security/20191028T085816Z/dists/buster/updates/main/binary-amd64/Packages.gz",
    sha256 = "dace61a2f1c4031f33dbc78e416a7211fad9946a3d997e96256561ed92b034be",
)

load("@rules_python//python:pip.bzl", "pip_import")

pip_import(
   name = "contrail_config_api_deps",
   requirements = "//contrail/configapi:requirements.txt",
)

load("@contrail_config_api_deps//:requirements.bzl", "pip_install")
pip_install()

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_m4",
    urls = ["https://github.com/jmillikin/rules_m4/releases/download/v0.2/rules_m4-v0.2.tar.xz"],
    sha256 = "c67fa9891bb19e9e6c1050003ba648d35383b8cb3c9572f397ad24040fb7f0eb",
)
load("@rules_m4//m4:m4.bzl", "m4_register_toolchains")
m4_register_toolchains()

http_archive(
    name = "rules_bison",
    urls = ["https://github.com/jmillikin/rules_bison/releases/download/v0.2/rules_bison-v0.2.tar.xz"],
    sha256 = "6ee9b396f450ca9753c3283944f9a6015b61227f8386893fb59d593455141481",
)
load("@rules_bison//bison:bison.bzl", "bison_register_toolchains")
bison_register_toolchains()

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_m4",
    urls = ["https://github.com/jmillikin/rules_m4/releases/download/v0.2/rules_m4-v0.2.tar.xz"],
    sha256 = "c67fa9891bb19e9e6c1050003ba648d35383b8cb3c9572f397ad24040fb7f0eb",
)
load("@rules_m4//m4:m4.bzl", "m4_register_toolchains")
m4_register_toolchains()

http_archive(
    name = "rules_flex",
    urls = ["https://github.com/jmillikin/rules_flex/releases/download/v0.2/rules_flex-v0.2.tar.xz"],
    sha256 = "f1685512937c2e33a7ebc4d5c6cf38ed282c2ce3b7a9c7c0b542db7e5db59d52",
)
load("@rules_flex//flex:flex.bzl", "flex_register_toolchains")
flex_register_toolchains()

CONTRAIL_COMMON_BUILD = """
filegroup(
    name = "src_common",
    srcs = glob([ "**/*" ]),
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "nodeinfo.sandesh",
    srcs = [ "base/sandesh/nodeinfo.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "process_info.sandesh",
    srcs = [ "base/sandesh/process_info.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "cpuinfo.sandesh",
    srcs = [ "base/sandesh/cpuinfo.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "io.sandesh",
    srcs = [ "io/io.sandesh" ],
    visibility = [ "//visibility:public" ],
)
py_library(
    name = "contrail_common",
    srcs = glob([ "**/*.py" ]),
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "sandesh.sandesh",
    srcs = [ "sandesh/library/common/sandesh.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "sandesh_uve.sandesh",
    srcs = [ "sandesh/library/common/sandesh_uve.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "derived_stats_results.sandesh",
    srcs = [ "sandesh/library/common/derived_stats_results.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "sandesh_alarm.sandesh",
    srcs = [ "sandesh/library/common/sandesh_alarm.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "sandesh_trace.sandesh",
    srcs = [ "sandesh/library/common/sandesh_trace.sandesh" ],
    visibility = [ "//visibility:public" ],
)
genrule(
    name = "sandesh_gen",
    srcs = [
                ":sandesh.sandesh",
                ":sandesh_uve.sandesh",
                ":sandesh_alarm.sandesh",
                ":sandesh_trace.sandesh",
                ":derived_stats_results.sandesh",
                ":io.sandesh",
		":process_info.sandesh",
           ],
    outs = [
                "sandesh/library/python/pysandesh/gen_py/sandesh/request_skeleton.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh/constants.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh/__init__.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh/ttypes.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh/http_request.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_alarm/request_skeleton.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_alarm/constants.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_alarm/__init__.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_alarm/ttypes.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_alarm/http_request.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_trace/request_skeleton.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_trace/constants.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_trace/__init__.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_trace/ttypes.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_trace/http_request.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/request_skeleton.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/constants.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/__init__.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/ttypes.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/http_request.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/request_skeleton.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/constants.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/__init__.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/ttypes.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/http_request.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/request_skeleton.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/constants.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/__init__.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/ttypes.py",
                "sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/http_request.py",
                "sandesh/library/python/pysandesh/gen_py/process_info/request_skeleton.py",
                "sandesh/library/python/pysandesh/gen_py/process_info/constants.py",
                "sandesh/library/python/pysandesh/gen_py/process_info/__init__.py",
                "sandesh/library/python/pysandesh/gen_py/process_info/ttypes.py",
                "sandesh/library/python/pysandesh/gen_py/process_info/http_request.py",
    ],
    cmd  = \"\"\"
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location :sandesh.sandesh)
    cp sandesh/request_skeleton.py $(location sandesh/library/python/pysandesh/gen_py/sandesh/request_skeleton.py)
    cp sandesh/constants.py $(location sandesh/library/python/pysandesh/gen_py/sandesh/constants.py)
    cp sandesh/__init__.py $(location sandesh/library/python/pysandesh/gen_py/sandesh/__init__.py)
    cp sandesh/ttypes.py $(location sandesh/library/python/pysandesh/gen_py/sandesh/ttypes.py)
    cp sandesh/http_request.py $(location sandesh/library/python/pysandesh/gen_py/sandesh/http_request.py)

    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location :sandesh_alarm.sandesh)
    cp sandesh_alarm/request_skeleton.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_alarm/request_skeleton.py)
    cp sandesh_alarm/constants.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_alarm/constants.py)
    cp sandesh_alarm/__init__.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_alarm/__init__.py)
    cp sandesh_alarm/ttypes.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_alarm/ttypes.py)
    cp sandesh_alarm/http_request.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_alarm/http_request.py)

    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location :sandesh_trace.sandesh)
    cp sandesh_trace/request_skeleton.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_trace/request_skeleton.py)
    cp sandesh_trace/constants.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_trace/constants.py)
    cp sandesh_trace/__init__.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_trace/__init__.py)
    cp sandesh_trace/ttypes.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_trace/ttypes.py)
    cp sandesh_trace/http_request.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_trace/http_request.py)

    mkdir -p io
    mkdir -p sandesh/library/common
    cp $(location :sandesh_uve.sandesh) .
    cp $(location :derived_stats_results.sandesh) sandesh/library/common
    cp $(location @contrail_common_repository//:io.sandesh) io
    cp ./$(location @sandesh_repository//:sandeshbin) .

    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . sandesh_uve.sandesh
    cp sandesh_uve/request_skeleton.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/request_skeleton.py)
    cp sandesh_uve/constants.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/constants.py)
    cp sandesh_uve/__init__.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/__init__.py)
    cp sandesh_uve/ttypes.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/ttypes.py)
    cp sandesh_uve/http_request.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location :derived_stats_results.sandesh)
    cp derived_stats_results/request_skeleton.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/request_skeleton.py)
    cp derived_stats_results/constants.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/constants.py)
    cp derived_stats_results/__init__.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/__init__.py)
    cp derived_stats_results/ttypes.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/ttypes.py)
    cp derived_stats_results/http_request.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/derived_stats_results/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location :io.sandesh)
    cp io/request_skeleton.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/request_skeleton.py)
    cp io/constants.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/constants.py)
    cp io/__init__.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/__init__.py)
    cp io/ttypes.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/ttypes.py)
    cp io/http_request.py $(location sandesh/library/python/pysandesh/gen_py/sandesh_uve/io/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location :process_info.sandesh)
    cp process_info/request_skeleton.py $(location sandesh/library/python/pysandesh/gen_py/process_info/request_skeleton.py)
    cp process_info/constants.py $(location sandesh/library/python/pysandesh/gen_py/process_info/constants.py)
    cp process_info/__init__.py $(location sandesh/library/python/pysandesh/gen_py/process_info/__init__.py)
    cp process_info/ttypes.py $(location sandesh/library/python/pysandesh/gen_py/process_info/ttypes.py)
    cp process_info/http_request.py $(location sandesh/library/python/pysandesh/gen_py/process_info/http_request.py)
    \"\"\",
    tools = ["@sandesh_repository//:sandeshbin"],
)
py_library(
    name = "genpysandesh",
    srcs = [":sandesh_gen"],
    visibility = [ "//visibility:public" ],
)
py_library(
    name = "pysandesh",
    srcs = glob([ "library/python/pysandesh/**/*.py" ]),
    imports = [ "sandesh/library/python" ],
    deps = [":genpysandesh"],
    visibility = [ "//visibility:public" ],
)
"""

CONTRAIL_BUILD = """
filegroup(
    name = "controller_src",
    srcs = glob([ "src/**/*" ]),
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "acl_sandesh",
    srcs = [ "src/config/uve/acl.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "cfgm_cpuinfo.sandesh",
    srcs = [ "src/config/uve/cfgm_cpuinfo.sandesh" ],
    visibility = [ "//visibility:public" ],
)

filegroup(
    name = "config_req.sandesh",
    srcs = [ "src/config/uve/config_req.sandesh" ],
    visibility = [ "//visibility:public" ],
)

filegroup(
    name = "msg_traces.sandesh",
    srcs = [ "src/config/uve/msg_traces.sandesh" ],
    visibility = [ "//visibility:public" ],
)

filegroup(
    name = "physical_router_config.sandesh",
    srcs = [ "src/config/uve/physical_router_config.sandesh" ],
    visibility = [ "//visibility:public" ],
)

filegroup(
    name = "physical_router.sandesh",
    srcs = [ "src/config/uve/physical_router.sandesh" ],
    visibility = [ "//visibility:public" ],
)

filegroup(
    name = "service_instance.sandesh",
    srcs = [ "src/config/uve/service_instance.sandesh" ],
    visibility = [ "//visibility:public" ],
)

filegroup(
    name = "service_status.sandesh",
    srcs = [ "src/config/uve/service_status.sandesh" ],
    visibility = [ "//visibility:public" ],
)

filegroup(
    name = "virtual_machine.sandesh",
    srcs = [ "src/config/uve/virtual_machine.sandesh" ],
    visibility = [ "//visibility:public" ],
)

filegroup(
    name = "virtual_network.sandesh",
    srcs = [ "src/config/uve/virtual_network.sandesh" ],
    visibility = [ "//visibility:public" ],
)

filegroup(
    name = "vnc_api.sandesh",
    srcs = [ "src/config/uve/vnc_api.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "greenlets.sandesh",
    srcs = [ "src/config/uve/greenlets.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "traces.sandesh",
    srcs = [ "src/config/api-server/traces.sandesh" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "vns.sandesh",
    srcs = [ "src/sandesh/common/vns.sandesh" ],
    visibility = [ "//visibility:public" ],
)
#exports_files(
#    ["src/config/uve/acl.sandesh"],
#    visibility = [ "//visibility:public" ],
#)
py_library(
    name = "sandesh_libs",
    srcs = [":sandesh_acl"],
)
py_library(
    name = "cfgm_common",
    srcs = glob([ "src/config/common/cfgm_common/**/*.py" ]),
    deps = [":sandesh_libs"],
    imports = [ 
                "src/config/common",
	      ],
    visibility = [ "//visibility:public" ],
)
genrule(
    name = "sandesh_acl",
    srcs = [
                "@contrail_common_repository//:src_common",
                "@contrail_common_repository//:nodeinfo.sandesh",
                "@contrail_common_repository//:process_info.sandesh",
                "@contrail_common_repository//:cpuinfo.sandesh",
                "@contrail_repository//:greenlets.sandesh",
                "@contrail_repository//:vns.sandesh",
                "@contrail_repository//:controller_src",
                "@contrail_repository//:acl_sandesh",
		"@contrail_repository//:cfgm_cpuinfo.sandesh",
                "@contrail_repository//:config_req.sandesh",
                "@contrail_repository//:msg_traces.sandesh",
                "@contrail_repository//:physical_router_config.sandesh",
                "@contrail_repository//:physical_router.sandesh",
                "@contrail_repository//:service_instance.sandesh",
		"@contrail_repository//:service_status.sandesh",
                "@contrail_repository//:virtual_machine.sandesh",
                "@contrail_repository//:virtual_network.sandesh",
                "@contrail_repository//:vnc_api.sandesh",
                "@contrail_repository//:traces.sandesh",
	   ],
    outs = [
                "common/sandesh_common/vns/request_skeleton.py",
                "common/sandesh_common/vns/constants.py",
                "common/sandesh_common/vns/__init__.py",
                "common/sandesh_common/vns/ttypes.py",
                "common/sandesh_common/vns/http_request.py",
                "acl/request_skeleton.py",
		"acl/constants.py",
		"acl/__init__.py",
		"acl/ttypes.py",
		"acl/http_request.py",
                "config_req/request_skeleton.py",
                "config_req/constants.py",
                "config_req/__init__.py",
                "config_req/ttypes.py",
                "config_req/http_request.py",
                "greenlets/request_skeleton.py",
                "greenlets/constants.py",
                "greenlets/__init__.py",
                "greenlets/ttypes.py",
                "greenlets/http_request.py",
                "msg_traces/request_skeleton.py",
                "msg_traces/constants.py",
                "msg_traces/__init__.py",
                "msg_traces/ttypes.py",
                "msg_traces/http_request.py",
                "physical_router_config/request_skeleton.py",
                "physical_router_config/constants.py",
                "physical_router_config/__init__.py",
                "physical_router_config/ttypes.py",
                "physical_router_config/http_request.py",
                "physical_router/request_skeleton.py",
                "physical_router/constants.py",
                "physical_router/__init__.py",
                "physical_router/ttypes.py",
                "physical_router/http_request.py",
                "service_instance/request_skeleton.py",
                "service_instance/constants.py",
                "service_instance/__init__.py",
                "service_instance/ttypes.py",
                "service_instance/http_request.py",
                "service_status/request_skeleton.py",
                "service_status/constants.py",
                "service_status/__init__.py",
                "service_status/ttypes.py",
                "service_status/http_request.py",
                "virtual_machine/request_skeleton.py",
                "virtual_machine/constants.py",
                "virtual_machine/__init__.py",
                "virtual_machine/ttypes.py",
                "virtual_machine/http_request.py",
                "virtual_network/request_skeleton.py",
                "virtual_network/constants.py",
                "virtual_network/__init__.py",
                "virtual_network/ttypes.py",
                "virtual_network/http_request.py",
                "src/config/common/cfgm_common/uve/vnc_api/request_skeleton.py",
                "src/config/common/cfgm_common/uve/vnc_api/constants.py",
                "src/config/common/cfgm_common/uve/vnc_api/__init__.py",
                "src/config/common/cfgm_common/uve/vnc_api/ttypes.py",
                "src/config/common/cfgm_common/uve/vnc_api/http_request.py",
                "src/config/common/cfgm_common/uve/nodeinfo/request_skeleton.py",
                "src/config/common/cfgm_common/uve/nodeinfo/constants.py",
                "src/config/common/cfgm_common/uve/nodeinfo/__init__.py",
                "src/config/common/cfgm_common/uve/nodeinfo/ttypes.py",
                "src/config/common/cfgm_common/uve/nodeinfo/http_request.py",
                "src/config/common/cfgm_common/uve/nodeinfo/process_info/request_skeleton.py",
                "src/config/common/cfgm_common/uve/nodeinfo/process_info/constants.py",
                "src/config/common/cfgm_common/uve/nodeinfo/process_info/__init__.py",
                "src/config/common/cfgm_common/uve/nodeinfo/process_info/ttypes.py",
                "src/config/common/cfgm_common/uve/nodeinfo/process_info/http_request.py",
                "src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/request_skeleton.py",
                "src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/constants.py",
                "src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/__init__.py",
                "src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/ttypes.py",
                "src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/http_request.py",
                "src/config/common/cfgm_common/uve/greenlets/request_skeleton.py",
                "src/config/common/cfgm_common/uve/greenlets/constants.py",
                "src/config/common/cfgm_common/uve/greenlets/__init__.py",
                "src/config/common/cfgm_common/uve/greenlets/ttypes.py",
                "src/config/common/cfgm_common/uve/greenlets/http_request.py",
                "src/config/api-server/vnc_cfg_api_server/sandesh/traces/request_skeleton.py",
                "src/config/api-server/vnc_cfg_api_server/sandesh/traces/constants.py",
                "src/config/api-server/vnc_cfg_api_server/sandesh/traces/__init__.py",
                "src/config/api-server/vnc_cfg_api_server/sandesh/traces/ttypes.py",
                "src/config/api-server/vnc_cfg_api_server/sandesh/traces/http_request.py",
                "src/config/common/cfgm_common/uve/cfgm_cpuinfo/request_skeleton.py",
                "src/config/common/cfgm_common/uve/cfgm_cpuinfo/constants.py",
                "src/config/common/cfgm_common/uve/cfgm_cpuinfo/__init__.py",
                "src/config/common/cfgm_common/uve/cfgm_cpuinfo/ttypes.py",
                "src/config/common/cfgm_common/uve/cfgm_cpuinfo/http_request.py",
    ],
    cmd  = \"\"\"
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:vns.sandesh)
    cp vns/request_skeleton.py $(location common/sandesh_common/vns/request_skeleton.py)
    cp vns/constants.py $(location common/sandesh_common/vns/constants.py)
    cp vns/__init__.py $(location common/sandesh_common/vns/__init__.py)
    cp vns/ttypes.py $(location common/sandesh_common/vns/ttypes.py)
    cp vns/http_request.py $(location common/sandesh_common/vns/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_common_repository//:process_info.sandesh)
    cp process_info/request_skeleton.py $(location src/config/common/cfgm_common/uve/nodeinfo/process_info/request_skeleton.py)
    cp process_info/constants.py $(location src/config/common/cfgm_common/uve/nodeinfo/process_info/constants.py)
    cp process_info/__init__.py $(location src/config/common/cfgm_common/uve/nodeinfo/process_info/__init__.py)
    cp process_info/ttypes.py $(location src/config/common/cfgm_common/uve/nodeinfo/process_info/ttypes.py)
    cp process_info/http_request.py $(location src/config/common/cfgm_common/uve/nodeinfo/process_info/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_common_repository//:cpuinfo.sandesh)
    cp cpuinfo/request_skeleton.py $(location src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/request_skeleton.py)
    cp cpuinfo/constants.py $(location src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/constants.py)
    cp cpuinfo/__init__.py $(location src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/__init__.py)
    cp cpuinfo/ttypes.py $(location src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/ttypes.py)
    cp cpuinfo/http_request.py $(location src/config/common/cfgm_common/uve/nodeinfo/cpuinfo/http_request.py)
    mkdir -p base/sandesh
    cp $(location @contrail_common_repository//:nodeinfo.sandesh) .
    cp $(location @contrail_common_repository//:process_info.sandesh) base/sandesh/
    cp $(location @contrail_common_repository//:cpuinfo.sandesh) base/sandesh/
    cp ./$(location @sandesh_repository//:sandeshbin) .
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . nodeinfo.sandesh
    #./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_common_repository//:nodeinfo.sandesh)
    cp nodeinfo/request_skeleton.py $(location src/config/common/cfgm_common/uve/nodeinfo/request_skeleton.py)
    cp nodeinfo/constants.py $(location src/config/common/cfgm_common/uve/nodeinfo/constants.py)
    cp nodeinfo/__init__.py $(location src/config/common/cfgm_common/uve/nodeinfo/__init__.py)
    cp nodeinfo/ttypes.py $(location src/config/common/cfgm_common/uve/nodeinfo/ttypes.py)
    cp nodeinfo/http_request.py $(location src/config/common/cfgm_common/uve/nodeinfo/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:acl_sandesh)
    cp acl/request_skeleton.py $(location acl/request_skeleton.py)
    cp acl/constants.py $(location acl/constants.py)
    cp acl/__init__.py $(location acl/__init__.py)
    cp acl/ttypes.py $(location acl/ttypes.py)
    cp acl/http_request.py $(location acl/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:config_req.sandesh)
    cp config_req/request_skeleton.py $(location config_req/request_skeleton.py)
    cp config_req/constants.py $(location config_req/constants.py)
    cp config_req/__init__.py $(location config_req/__init__.py)
    cp config_req/ttypes.py $(location config_req/ttypes.py)
    cp config_req/http_request.py $(location config_req/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:greenlets.sandesh)
    cp greenlets/request_skeleton.py $(location greenlets/request_skeleton.py)
    cp greenlets/constants.py $(location greenlets/constants.py)
    cp greenlets/__init__.py $(location greenlets/__init__.py)
    cp greenlets/ttypes.py $(location greenlets/ttypes.py)
    cp greenlets/http_request.py $(location greenlets/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:msg_traces.sandesh)
    cp msg_traces/request_skeleton.py $(location msg_traces/request_skeleton.py)
    cp msg_traces/constants.py $(location msg_traces/constants.py)
    cp msg_traces/__init__.py $(location msg_traces/__init__.py)
    cp msg_traces/ttypes.py $(location msg_traces/ttypes.py)
    cp msg_traces/http_request.py $(location msg_traces/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:physical_router_config.sandesh)
    cp physical_router_config/request_skeleton.py $(location physical_router_config/request_skeleton.py)
    cp physical_router_config/constants.py $(location physical_router_config/constants.py)
    cp physical_router_config/__init__.py $(location physical_router_config/__init__.py)
    cp physical_router_config/ttypes.py $(location physical_router_config/ttypes.py)
    cp physical_router_config/http_request.py $(location physical_router_config/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:physical_router_config.sandesh)
    cp physical_router_config/request_skeleton.py $(location physical_router_config/request_skeleton.py)
    cp physical_router_config/constants.py $(location physical_router_config/constants.py)
    cp physical_router_config/__init__.py $(location physical_router_config/__init__.py)
    cp physical_router_config/ttypes.py $(location physical_router_config/ttypes.py)
    cp physical_router_config/http_request.py $(location physical_router_config/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:physical_router.sandesh)
    cp physical_router/request_skeleton.py $(location physical_router/request_skeleton.py)
    cp physical_router/constants.py $(location physical_router/constants.py)
    cp physical_router/__init__.py $(location physical_router/__init__.py)
    cp physical_router/ttypes.py $(location physical_router/ttypes.py)
    cp physical_router/http_request.py $(location physical_router/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:service_instance.sandesh)
    cp service_instance/request_skeleton.py $(location service_instance/request_skeleton.py)
    cp service_instance/constants.py $(location service_instance/constants.py)
    cp service_instance/__init__.py $(location service_instance/__init__.py)
    cp service_instance/ttypes.py $(location service_instance/ttypes.py)
    cp service_instance/http_request.py $(location service_instance/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:service_status.sandesh)
    cp service_status/request_skeleton.py $(location service_status/request_skeleton.py)
    cp service_status/constants.py $(location service_status/constants.py)
    cp service_status/__init__.py $(location service_status/__init__.py)
    cp service_status/ttypes.py $(location service_status/ttypes.py)
    cp service_status/http_request.py $(location service_status/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:virtual_machine.sandesh)
    cp virtual_machine/request_skeleton.py $(location virtual_machine/request_skeleton.py)
    cp virtual_machine/constants.py $(location virtual_machine/constants.py)
    cp virtual_machine/__init__.py $(location virtual_machine/__init__.py)
    cp virtual_machine/ttypes.py $(location virtual_machine/ttypes.py)
    cp virtual_machine/http_request.py $(location virtual_machine/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:virtual_network.sandesh)
    cp virtual_network/request_skeleton.py $(location virtual_network/request_skeleton.py)
    cp virtual_network/constants.py $(location virtual_network/constants.py)
    cp virtual_network/__init__.py $(location virtual_network/__init__.py)
    cp virtual_network/ttypes.py $(location virtual_network/ttypes.py)
    cp virtual_network/http_request.py $(location virtual_network/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:vnc_api.sandesh)
    cp vnc_api/request_skeleton.py $(location src/config/common/cfgm_common/uve/vnc_api/request_skeleton.py)
    cp vnc_api/constants.py $(location src/config/common/cfgm_common/uve/vnc_api/constants.py)
    cp vnc_api/__init__.py $(location src/config/common/cfgm_common/uve/vnc_api/__init__.py)
    cp vnc_api/ttypes.py $(location src/config/common/cfgm_common/uve/vnc_api/ttypes.py)
    cp vnc_api/http_request.py $(location src/config/common/cfgm_common/uve/vnc_api/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:greenlets.sandesh)
    cp greenlets/request_skeleton.py $(location src/config/common/cfgm_common/uve/greenlets/request_skeleton.py)
    cp greenlets/constants.py $(location src/config/common/cfgm_common/uve/greenlets/constants.py)
    cp greenlets/__init__.py $(location src/config/common/cfgm_common/uve/greenlets/__init__.py)
    cp greenlets/ttypes.py $(location src/config/common/cfgm_common/uve/greenlets/ttypes.py)
    cp greenlets/http_request.py $(location src/config/common/cfgm_common/uve/greenlets/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:traces.sandesh)
    cp traces/request_skeleton.py $(location src/config/api-server/vnc_cfg_api_server/sandesh/traces/request_skeleton.py)
    cp traces/constants.py $(location src/config/api-server/vnc_cfg_api_server/sandesh/traces/constants.py)
    cp traces/__init__.py $(location src/config/api-server/vnc_cfg_api_server/sandesh/traces/__init__.py)
    cp traces/ttypes.py $(location src/config/api-server/vnc_cfg_api_server/sandesh/traces/ttypes.py)
    cp traces/http_request.py $(location src/config/api-server/vnc_cfg_api_server/sandesh/traces/http_request.py)
    ./$(location @sandesh_repository//:sandeshbin) --gen py:new_style --out . $(location @contrail_repository//:cfgm_cpuinfo.sandesh)
    cp cfgm_cpuinfo/request_skeleton.py $(location src/config/common/cfgm_common/uve/cfgm_cpuinfo/request_skeleton.py)
    cp cfgm_cpuinfo/constants.py $(location src/config/common/cfgm_common/uve/cfgm_cpuinfo/constants.py)
    cp cfgm_cpuinfo/__init__.py $(location src/config/common/cfgm_common/uve/cfgm_cpuinfo/__init__.py)
    cp cfgm_cpuinfo/ttypes.py $(location src/config/common/cfgm_common/uve/cfgm_cpuinfo/ttypes.py)
    cp cfgm_cpuinfo/http_request.py $(location src/config/common/cfgm_common/uve/cfgm_cpuinfo/http_request.py)
    \"\"\",
    tools = ["@sandesh_repository//:sandeshbin"],
)
genrule(
  name = "buildinfo",
  srcs = [],
  outs = ["src/config/common/cfgm_common/buildinfo.py"],
  cmd = \"\"\"
  echo build_info = '"'{"\ "'"'build-info"\ "'"' : [{"\ "'"'build-version"\ "'"' : "\ "'"'bla"\ "'"', "\ "'"'build-time"\ "'"' : "\ "'"'blabla"\ "'"', "\ "'"'build-user"\ "'"' : "\ "'"'blabla"\ "'"', "\ "'"'build-hostname"\ "'"' : "\ "'"'blabla"\ "'"', '"' \";\" |sed 's/ //g' > $@
  cat $@
#echo "build_info = \\\"{\\"build-info\\" : [{\\"build-version\\" : \\"1911\\", \\"build-time\\" : \\"2019-11-07 00:32:24.968612\\", \\"build-user\\" : \\"root\\", \\"build-hostname\\" : \\"15af5590982a\\", \\";" > $@
#echo " \" \\" \\\" \\\\" " > $@
#echo "\ "'"' |sed 's/ //g'
\"\"\",
)
py_library(
    name = "buildinfo.py",
    srcs = [":buildinfo"],
)
py_library(
    name = "vnc_cfg_api_server",
    srcs = glob([ "src/config/api-server/vnc_cfg_api_server/**/*.py" ]),
    imports = [ 
	        "common",
		"src/config/api-server",
		"src/config/common",
	      ],
    deps = [":buildinfo.py"],
    visibility = [ "//visibility:public" ],
)
exports_files(["src/config/api-server/vnc_cfg_api_server/api_server.py"])
"""

CONTRAIL_API_BUILD = """
py_library(
    name = "vnc_api",
    srcs = glob([ "api-lib/vnc_api/**/*.py" ]),
    imports = [ "api-lib" ],
    visibility = [ "//visibility:public" ],
)
#exports_files(["api-lib/vnc_api/test.py"],
"""

SANDESH_BUILD = """
load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library", "cc_test")
load("@rules_bison//bison:bison.bzl", "bison_cc_library")
load("@rules_bison//bison:bison.bzl", "bison")
load("@rules_flex//flex:flex.bzl", "flex")
filegroup(
    name = "sandesh_headers",
    srcs = glob([ "compiler/**/*.h" ]),
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "main_cc",
    srcs = [ "compiler/main.cc" ],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "md5_c",
    srcs = ["compiler/md5.c"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "sandeshy_yy",
    srcs = ["compiler/sandeshy.yy"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "sandeshl_ll",
    srcs = ["compiler/sandeshl.ll"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "t_cpp_generator_cc",
    srcs = ["compiler/generate/t_cpp_generator.cc"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "t_html_generator_cc",
    srcs = ["compiler/generate/t_html_generator.cc"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "t_generator_cc",
    srcs = ["compiler/generate/t_generator.cc"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "t_xsd_generator_cc",
    srcs = ["compiler/generate/t_xsd_generator.cc"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "t_c_generator_cc",
    srcs = ["compiler/generate/t_c_generator.cc"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "t_py_generator_cc",
    srcs = ["compiler/generate/t_py_generator.cc"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "t_doc_generator_cc",
    srcs = ["compiler/generate/t_doc_generator.cc"],
    visibility = [ "//visibility:public" ],
)
filegroup(
    name = "parse_cc",
    srcs = ["compiler/parse/parse.cc"],
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "main",
    srcs = [ ":main_cc", ],
    hdrs = [ ":sandesh_headers", ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "md5",
    srcs = [ ":md5_c", ],
    hdrs = [ ":sandesh_headers", ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
#bison(
#    name = "sandeshy_bison",
#    src = ":sandeshy_yy"
#)
genrule(
    name = "sandeshy_bison",
    srcs = [":sandeshy_yy"],
    outs = ["sandeshy.cc","sandeshy.hh"],
    #cmd = "bison -d --output=$@ $<",
    #cmd = "$(BISON) -d -o $@ $<",
    cmd = "$(BISON) --defines=$(location sandeshy.hh) -o $(location sandeshy.cc) $<",
    toolchains = [
        "@rules_bison//bison:current_bison_toolchain",
        "@rules_m4//m4:current_m4_toolchain",
    ],
)
cc_library(
    name = "sandeshy",
    srcs = [ ":sandeshy_bison" ],
    hdrs = [ ":sandesh_headers", ],
    copts = ["--std=c99 -Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
genrule(
    name = "sandeshl_flex",
    srcs = [":sandeshl_ll"],
    outs = ["sandeshl.cc"],
    cmd = "flex -w -t $< > $@",
    #cmd = "$(FLEX) -w -t $< > $@",
    toolchains = [
        "@rules_flex//flex:current_flex_toolchain",
        "@rules_m4//m4:current_m4_toolchain",
    ],
)
#flex(
#    name = "sandeshl_flex",
#    src = ":sandeshl_ll",
#)
cc_library(
    name = "sandeshl",
    srcs = [ ":sandeshl_flex" ],
    hdrs = [ ":sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    deps = [":sandeshy"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)

cc_library(
    name = "t_cpp_generator",
    srcs = [ ":t_cpp_generator_cc" ],
    hdrs = [ ":sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_html_generator",
    srcs = [ ":t_html_generator_cc" ],
    hdrs = [ ":sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_generator",
    srcs = [ ":t_generator_cc" ],
    hdrs = [ ":sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_xsd_generator",
    srcs = [ ":t_xsd_generator_cc" ],
    hdrs = [ ":sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_c_generator",
    srcs = [ ":t_c_generator_cc" ],
    hdrs = [ ":sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_py_generator",
    srcs = [ ":t_py_generator_cc" ],
    hdrs = [ ":sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "t_doc_generator",
    srcs = [ ":t_doc_generator_cc" ],
    hdrs = [ ":sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    visibility = [ "//visibility:public" ],
)
cc_library(
    name = "parse",
    srcs = [ ":parse_cc",":md5" ],
    hdrs = [ ":sandesh_headers" ],
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    linkstatic = 1,
    alwayslink = 1,
    deps = [":md5"],
    visibility = [ "//visibility:public" ],
)

cc_binary(
    name = "sandeshbin",
    copts = ["-Iexternal/sandesh_repository/compiler","-c","-O0","-DDEBUG","-g","-DSANDESH"],
    deps = [
             ":main",
             ":md5",
             ":sandeshy",
             ":sandeshl",
             ":t_cpp_generator",
             ":t_html_generator",
             ":t_generator",
             ":t_xsd_generator",
             ":t_c_generator",
             ":t_py_generator",
             ":t_doc_generator",
             ":parse",
        ],
    linkstatic = 1,
    visibility = [ "//visibility:public" ],
)
"""

new_git_repository(
    name = "sandesh_repository",
    remote = "https://github.com/Juniper/contrail-sandesh.git",
    branch = "master",
    build_file_content = SANDESH_BUILD
)
new_git_repository(
    name = "contrail_repository",
    remote = "https://github.com/Juniper/contrail-controller.git",
    branch = "master",
    patch_cmds = [
		    "mv src/config/api-server/vnc_cfg_api_server/vnc_cfg_api_server.py src/config/api-server/vnc_cfg_api_server/api_server.py",
		 ],
    build_file_content = CONTRAIL_BUILD
)
new_git_repository(
    name = "contrail_common_repository",
    remote = "https://github.com/Juniper/contrail-common.git",
    branch = "master",
    build_file_content = CONTRAIL_COMMON_BUILD
)
new_git_repository(
    name = "contrail_api_repository",
    remote = "https://github.com/Juniper/contrail-api-client.git",
    branch = "master",
    patch_cmds = [
		    "mkdir api-lib/vnc_api/{gen,doc}",
		    "cp generateds/{generatedssuper.py,cfixture.py} api-lib/vnc_api/gen",
		    "HEAT_BUILDTOP=\"$(pwd)\" generateds/generateDS.py -f -o api-lib/vnc_api/gen/resource -g ifmap-frontend schema/all_cfg.xsd"
		 ],
    build_file_content = CONTRAIL_API_BUILD,
)
