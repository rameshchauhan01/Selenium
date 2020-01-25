**find_element_by_tag_name() or find_elements_by_tag_name() :**  
The method is useful when we want to find elements using their tag name. For example, to find all the <tr> tags in a table to find the number of rows.
<ul class=“promos”> <li> <a href=“http://demo.magentocommerce.com/home-decor.html”> <img src=”/media/wysiwyg/homepage-three-column-promo-01B.png”
alt=“Physical &amp; Virtual Gift Cards”></a> </li> <li> <a href=“http://demo.magentocommerce.com/vip.html”> <img src=”/media/wysiwyg/homepage-three-column-promo-02.png”
alt=“Shop Private Sales - Members Only”> </a> </li>< li> <a href=“http://demo.magentocommerce.com/accessories/bagsluggage.html”>
<img src=”/media/wysiwyg/homepage-three-column-promo-03.png” alt=“Travel Gear for Every Occasion”> </a> </li> </ul>  
We will use the find_elements_by_tag_name() method to get all the images. In this example, we will first find the list of banners    
implemented as ul or unordered lists using the find_element_by_class_name() method and then get all the img or image elements
by calling the find_elements_by_tag_name() method on the banners list: <br>  
def test_count_of_promo_banners_images(self):  <br>
#get promo banner list   <br>
banner_list = self.driver.find_element_by_class_name(“promos”) <br>   
#get images from the banner_list  <br>  
banners = banner_list.find_elements_by_tag_name(“img”)   <br>  
#check there are tags displayed on the page   <br>   
self.assertEqual(3, len(banners))  <br>   

**find_element_by_xpath():**   
We can also use defined attributes other than the ID, name, or class with XPath queries. We can also find
elements with the help of a partial check on attribute values using XPath functions such as
starts-with(), contains(), and ends-with(). <br>

**find_elements_by_partial_link_text:**  
def test_account_links(self):  
#get the all the links with Account text in it   
account_links = self.driver.\find_elements_by_partial_link_text(“ACCOUNT”)     
#check Account and My Account link is displayed/visible in the Home page footer  
self.assertTrue(2, len(account_links))
