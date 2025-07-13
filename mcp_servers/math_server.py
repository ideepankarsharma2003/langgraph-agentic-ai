from mcp.server.fastmcp import FastMCP

mcp= FastMCP("Math")

@mcp.tool()
def add(a:float, b:float)->float:
    """return sum of two numbers"""
    return a+b

@mcp.tool()
def multiply(a:float, b:float)->float:
    """return product of two numbers"""
    return a*b

if __name__=='__main__':
    mcp.run(transport="stdio")
    # stdio-> use stdin/stdout, terminal to receive to tool function calls 
    # streamable-http-> http server 
    