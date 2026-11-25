import csv
from mcp.server.fastmcp import FastMCP
 
mcp = FastMCP("pharmacy-stock")
DATA = "data/pharmacy_stock.csv"
 
def load():
    with open(DATA, newline="") as f:
        return list(csv.DictReader(f))
 
@mcp.tool()
def check_stock(item: str, strength: str = "") -> list[dict]:
    """Return stock rows whose item name contains item (and strength, if given)."""
    rows = [r for r in load() if item.lower() in r["item"].lower()]
    if strength:
        rows = [r for r in rows if strength.lower() in r["strength"].lower()]
    return rows
 
if __name__ == "__main__":
    mcp.run()
