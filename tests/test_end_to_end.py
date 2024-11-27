from scripts.regenerate_models import main
import os

def test_end_to_end(tmpdir, monkeypatch):
    output_dir = tmpdir.mkdir("autogenerated")
    template_path = "src/cold/models/templates/pydantic_template.jinja2"

    # Monkeypatch output directory and template path
    monkeypatch.setattr("scripts.regenerate_models.OUTPUT_DIR", str(output_dir))
    monkeypatch.setattr("scripts.regenerate_models.TEMPLATE_PATH", template_path)

    # Run the script
    main()

    # Check the output
    files = os.listdir(str(output_dir))
    assert len(files) > 0, "No models generated during end-to-end test"
    assert "__init__.py" in files, "Lazy loader not generated"
