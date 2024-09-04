Bazel is an open-source build and test tool developed by Google. It is designed to handle large codebases with complex dependencies and provides fast and reliable builds. Bazel supports a wide range of languages, including Python, Java, C++, and more. It also offers powerful features like incremental builds, caching, and parallel execution.

Build the Library

bazel build //lib:helper_lib

Run unit tests

bazel test //tests:test_helper

Run performance test

bazel test //tests:test_performance
