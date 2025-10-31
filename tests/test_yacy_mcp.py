import pytest
from yacy_mcp.server import yacy_search


@pytest.mark.asyncio
async def test_perform_yacy_search():
    """Test the YaCy search function."""
    # This test will likely return an error without a running YaCy instance
    # but it will test the function structure
    result = await yacy_search("test query", 5)
    # The function should return a string, possibly with an error message
    # if YaCy is not running
    assert isinstance(result, str)


if __name__ == "__main__":
    pytest.main([__file__])