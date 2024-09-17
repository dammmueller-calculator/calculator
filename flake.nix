{
  description = "Python development environment with PyQt6";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      with pkgs;
      {
        devShells.default = mkShell {
          buildInputs = [
            python3
            python3Packages.pip
            python3Packages.pyqt6
            gcc
          ];

          shellHook = ''
            export PYTHONPATH="${python3Packages.pyqt6}/${python3.sitePackages}:$PYTHONPATH"
            export LD_LIBRARY_PATH="${gcc}/lib:$LD_LIBRARY_PATH"
          '';
        };
      }
    );
}
