import dash_bootstrap_components as dbc

def Navbar():
    navbar = dbc.NavbarSimple(children=[
                dbc.NavItem(dbc.NavLink("Population", href="/time-series")),
                dbc.NavItem(dbc.NavLink("Population2", href="/time-series")),
                dbc.DropdownMenu(nav=True,
                in_navbar=True,
                label="Menu",
                children=[dbc.DropdownMenuItem("Entry 1", href = "/firstplot"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),],),
                dbc.DropdownMenu(nav=True,
                in_navbar=True,
                label="Menu2",
                children=[dbc.DropdownMenuItem("Entry 1", href = "/firstplot"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),],),
                ],brand="Home", brand_href="/home",sticky="top",
              )
    return navbar
