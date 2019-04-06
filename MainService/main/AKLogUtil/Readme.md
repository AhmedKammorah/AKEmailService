# My Data Utilities 

## Logs utils
### How To use 

	


```
	from ak_data_utilities.AKLogUtil.AKLogUtil import getLogger
	# at the beginning of the class 
	logger = getLogger(<Your Service Name>)

	logger.debug("Service start")
	logger.info("Service close")

```