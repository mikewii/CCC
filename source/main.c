#include "fun.h"
#include <3ds.h>
#include "csvc.h"
#include <string.h>

#define CUR_PROCESS_HANDLE 0xFFFF8001
#define PERM MEMPERM_READ | MEMPERM_WRITE // | MEMPERM_EXECUTE
#define MEM_LIMIT 0x40000000

/* test code
* map memory from off to off: working
* svcMapProcessMemoryEx(CUR_PROCESS_HANDLE, 0x07000000, CUR_PROCESS_HANDLE, 0x00100000, 0x1000);
*
* dunno what it supose to do: not working
* svcMapProcessMemory(procHandle, 0x06000000, 0x1000);
*/

void fun() {
	u32 CProcID;
	Handle CProcHandle;
	
	/* Obtain current process handle: */
	svcGetProcessId(&CProcID, CUR_PROCESS_HANDLE);
	svcOpenProcess(&CProcHandle, CProcID);

	/* Expose mapped memory */
	checkMemory(CProcHandle);
	
	//launchApplet(CProcHandle);
	//launchApplet(CProcHandle);
	//mcuHwcTest();
}

void checkMemory(Handle handle) {
	u32 address = 0;
	MemInfo memi;
	PageInfo pagei;
	
	while (address < MEM_LIMIT ///< Limit to check for regions
        && R_SUCCEEDED(svcQueryProcessMemory(&memi, &pagei, handle, address)))
		{
			// Update the address for next region
			address = memi.base_addr + memi.size;
			
			// Set rw- permission to those without any
			if (memi.state != MEMSTATE_FREE && (memi.perm == 0))
			{
				svcControlProcessMemory(handle, memi.base_addr, memi.base_addr, memi.size, MEMOP_PROT, PERM);
			}
		}
	
}

void launchApplet( Handle handle ) {
	static errorConf *err;
	
	errorInit(err, ERROR_EULA, CFG_LANGUAGE_EN);
	errorDisp(err);
}

void mcuHwcTest() {
	srvPmInit();
	srvPmExit();
	//mcuHwcInit();
	//cuHwcExit();
}