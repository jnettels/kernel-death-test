When pandas.read_excel(), df.to_excel(), geopandas.read_file() and gdf.to_file()
are called in a certain order in different environments, pd.read_excel() sometimes
casues "Kernel has died" errors.

This repository is for trying to reproduce the issue and narrow down the
package(s) that cause it.

I have a minimal environment that works fine, and a "full" environment I need
for other purposes, where the issue happens.
Ubuntu is always fine, the issue is only on windows.
