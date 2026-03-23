from ai_rag.scripts.demo_rag_pipeline import fake_embedding, synthesize_response


def test_fake_embedding_shape() -> None:
    assert len(fake_embedding("hello")) == 24


def test_synthesis_contains_query() -> None:
    query = "test"
    out = synthesize_response(query, ["a", "b"])
    assert "Query: test" in out
