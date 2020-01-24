# SearchContext vs By
Before going into deep lets unsertand the implements and extends
- class implements interface
- class extends class
- interfce entends interface <br>
In Selenium you have an interface called a SearchContext and then you have the By class.

A SearchContext can be a WebElement or a WebDriver

Now you have two options to find an element (using pseudo-code):

1) SearchContext.findElement(By...)

or

2) By.findElement(SearchContext...)

Both do the same thing!

Say in your case you have a driver and the By variable like this:

WebDriver driver = new FirefoxDriver();
By addButtonLocator = By.id("asdf");
now you can find your element in two ways:

1) driver.findElement(addButtonLocator);

or

2) addButtonLocator.findElement(driver);

Again! Both do the same thing, it's just another way to "read" these expressions like this:

1) "take the driver and search for an element using this By-statement"
or

2) "take the By-statement and search for an element that fits this statement within driver"


As said before, instead of a driver you can have a smaller scope if you use an already identified element
