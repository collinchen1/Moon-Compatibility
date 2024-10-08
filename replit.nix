{pkgs}: {
  deps = [
    pkgs.glibcLocales
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.glibcLocales
    ];
  };
}
