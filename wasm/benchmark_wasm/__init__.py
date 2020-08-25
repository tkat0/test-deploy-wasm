try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

import wasmtime


def init():
    # TODO: loader can not load module using WASI
    #   https://github.com/bytecodealliance/wasmtime-py/pull/44
    # import wasmtime.loader
    # import benchmark_wasm_wasi

    wasm_cfg = wasmtime.Config()
    wasm_cfg.cache = True

    wasi_cfg = wasmtime.WasiConfig()
    store = wasmtime.Store(wasmtime.Engine(wasm_cfg))
    linker = wasmtime.Linker(store)
    linker.define_wasi(wasmtime.WasiInstance(store,
                                             "wasi_snapshot_preview1", wasi_cfg))
    wasm = pkg_resources.read_binary(__package__, "benchmark_wasm.wasm")
    instance = linker.instantiate(wasmtime.Module(store.engine, wasm))
    return instance

instance = init()

