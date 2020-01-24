# Browser Properties implementation
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

# Browser Method implementation
The WebDriver class implements various methods to interact with the browser window,
web pages, and the elements on these pages:

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

# WeElement class properties
The WebElement class implements the following properties:

|Property/attribute| Description| Example|
|---------|--------|-----|
|size| This gets the size of the element| element.size|
|tag_name| This gets this element’s HTML tag name| element.tag_name|
|text| This gets the text of the element| element.text|

# WebElement class methos
The WebElement class implements the following methods:

|Method| Description |Example|
|------|--------|--------|
|clear()| This clears the content of the textbox or text area | element. element.clear()|
|click()| This clicks the element. |element.click()|
|get_attribute(name)| This gets the attribute value from the element.name is the name of the attribute.|element.get_attribute(“value”)Or element.get_attribute(“maxlength”)|
|is_displayed()| This checks whether the element is visible to the user.| element.is_displayed()|
|is_enabled()| This checks whether the element is enabled.| element.is_enabled()|
|is_selected()| This checks whether the element is selected. This method is used to check the selection of a radio button or checkbox.|element.is_selected()|
|send_keys(*value)| This simulates typing into the element. or setting form fields.|element.send_keys(“foo”)|
|submit()| This submits a form. If you call this method on an element, it will submit the parent form. |element.submit()|
|value_of_css_property(property_name)| This gets the value of a CSS property.|element.value_of_css_property(“backgroundcolor”)|

# find element methods:
Selenium provides eight find_element_by methods to locate elements. In this section, we
will see each one of them in detail. The following table lists find_element_by methods:

|Method| Description|Example|
|-----|------|------|
|find_element_by_id(id)|This method finds an element by the ID attribute|driver.find_element_by_id(‘search’)|
|find_element_by_name(name)|| driver.find_element_by_name(‘q’)|
|find_element_by_class_name(name)|| driver.find_element_by_class_name(‘input-text’)|
|find_element_by_tag_name(name)|| driver.find_element_by_tag_name(‘input’)|
|find_element_by_xpath(xpath)|| driver.find_element_by_xpath(‘//form[0]/div[0]/input[0]’)|
|find_element_by_css_selector(css_selector)|| driver.find_element_by_css_selector(‘#search’)|
|find_element_by_link_text(link_text)|| driver.find_element_by_link_text(‘Log In’)|
|find_element_by_partial_link_text(link_text)|| driver.find_element_by_partial_link_text(‘Log’)|

