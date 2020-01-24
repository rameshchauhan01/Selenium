# SearchContext vs By
Before going into deep lets unsertand the interface and abstract
- class implements interface
- class extends class
- interfce entends interface <br>
**Interface:** <br>
Like a class, an interface can have methods and variables, but the methods declared in an interface are by default abstract (only method signature, no body). <br>
**Abstract class and method:**<br>
A class which contains one or abstract methods is called an abstract class. An abstract method is a method that has declaration but not has any implementation. Abstract classes are not able to instantiated and it needs subclasses to provide implementations for those abstract methods which are defined in abstract classes<br>

Abstract classes allow partially to implement classes when it completely implements all methods in a class, then it is called interface.<br>  **1.Type of methods:** Interface can have only abstract methods. Abstract class can have abstract and non-abstract methods. From Java 8, it can have default and static methods also.  
**2.Final Variables:** Variables declared in a Java interface are by default final. An abstract class may contain non-final variables.
Type of variables: Abstract class can have final, non-final, static and non-static variables. Interface has only static and final variables.  
**3.Implementation:** Abstract class can provide the implementation of interface. Interface can’t provide the implementation of abstract class.  
**4.Inheritance vs Abstraction:** A Java interface can be implemented using keyword “implements” and abstract class can be extended using keyword “extends”.  
**5.Multiple implementation:** An interface can extend another Java interface only, an abstract class can extend another Java class and implement multiple Java interfaces.  
**6.Accessibility of Data Members:** Members of a Java interface are public by default. A Java abstract class can have class members like private, protected, etc.  
*I write an Interface with abstract methods I can send a message to all the browser companies i.e the third party companies to provide their implementation classes for my Interface. That’s where you have separate class files for FirefoxDriver , ChromeDriver etc. And these will implement the abstract methods of WebDriver interface in their way.*     
Example:
WebDriver driver = New FireFoxDriver();
  
implementing rules of interface WebDriver over the third party browser class files Firefox. FirefoxDriver() methods are defined in the class files FirefoxDriver.    
**SearchContext vs By:**
In Selenium you have an interface called a SearchContext and then you have the By class.
A SearchContext can be a WebElement or a WebDriver  
Example:  
driver.find_element(By.ID, "some_id");
So using Page Object pattern is the reason why you might need **find_element() + By instead of find_element_by_...().**  
1) SearchContext.find_element(By...)
or
2) By.find_element(SearchContext...)
Both do the same thing!

1) driver.find_element(By.ID, "some_id");  
or  
2) (By.ID, "some_id").find_element(driver);  
Again! Both do the same thing, it's just another way to "read" these expressions like this:  
1) "take the driver and search for an element using this By-statement"  
or  
2) "take the By-statement and search for an element that fits this statement within driver"

