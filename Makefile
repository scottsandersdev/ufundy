install-libs:
	# pip install everything in lib_requirements.txt to lib
	if [ -f lib_requirements.txt ]; then \
		if [ -f ~/.pydistutils.cfg.backup ]; then \
			cp ~/.pydistutils.cfg.backup ~/.pydistutils.cfg; \
		fi; \
		pip install -t lib -r lib_requirements.txt; \
		if [ -f ~/.pydistutils.cfg ]; then \
			rm ~/.pydistutils.cfg; \
		fi; \
	fi;
