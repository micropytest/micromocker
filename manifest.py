package("micromocker")
metadata(version="2026.6.1")

# dep libraries
add_library("lib", "deps/lib")

# dep freezing
require("abc")
require("inspect")
require("typing", library="lib")
