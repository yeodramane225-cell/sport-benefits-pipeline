def test_transform_import():
    from src.processing.transform import run_transform
    assert callable(run_transform)

