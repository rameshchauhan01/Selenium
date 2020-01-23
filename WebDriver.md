The WebDriver class implements the following properties for accessing the browser:

| Property | attribute Description | Example |
| ---------| ----------------------| --------|
|current_url| This gets the URL of the current page displayed in the browser| driver.current_url|
|current_window_handle| This gets the handle of the current window |driver.current_window_handle|
|name |This gets the name of the underlying browser for this instance| driver.name|
|orientation |This gets the current orientation of the device |driver.orientation|
|page_source | This gets the source of the current page |driver.page_source|
|title |This gets the title of the current page |driver.title|
|window_handles | This gets the handles of all windows within the current sessio|n driver.window_handles|

The WebDriver class implements the following properties for accessing the browser:

| Method | Description      | Example |
|------|--------------|-------|
|back()| This goes one step backward in the browser history in the current session.| driver.back()|
|close() |This closes the current browser window. | driver.close()|
|forward() | This goes one step forward in the browser history in the current session.| driver.forward()|
|get(url)| This navigates and loads a web page in the current browser session. url is the address of the website or web page to navigate | driver.get(“http://www.google.com”)|
|maximize_window() |This maximizes the current browser window.| driver.maximize_window()|
|quit()| This quits the driver and closes all the associated windows.| driver.quit()|
|refresh()| This refreshes the current page displayed in the browser.| driver.refresh()|
|switch_to.active_element()| This returns the element with focus or the body if nothing else has focus.| driver.switch_to_active_element()|
|Switch.to_alert()| This switches the focus to an alert on the page.| driver.switch_to_alert()|
|switch_to.default_content()| This switches the focus to the default frame.| driver.switch_to_default_content()|
|switch_to.frame(frame_reference) |This switches the focus to the specified frame, by index, name, or web element.This method also works on IFRAMES.frame_reference: This is the name of the window to switch to, an integer representing the index, or a web element that is a frame to switch to |driver.switch_to_frame(‘frame_name’)|
|switch_to.window(window_name)| This switches focus to the specified window. window_name is the name or window handle of the window to switch to.|driver.switch_to_window(‘main’)|
|implicitly_wait(time_to_wait)|This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete. This method only needs to be called one time per session. To set the timeout for calls to execute_async_script, see set_script_timeout.time_to_wait is the amount of time to wait (in seconds).||
|set_page_load_timeout(time_to_wait)| This sets the amount of time to wait for a page load to complete. time_to_wait is the amount of time to wait (in seconds).|driver.set_page_load_timeout(30)|
|set_script_timeout(time_to_wait)| This sets the amount of time that the script should wait during an execute_async_script call before throwing an error.time_to_wait is the amount of time to wait (in seconds).|driver.set_script_timeout(30)|
