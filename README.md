<!-- Add banner here -->

# Flipkart Grid 3.0
**Team Name**: Chemistry Gods

<!-- Add buttons here -->

<!-- Describe your project in brief -->

<!-- The project title should be self explanotory and try not to make it a mouthful. (Although exceptions exist- **awesome-readme-writing-guide-for-open-source-projects** - would have been a cool name)

Add a cover/banner image for your README. **Why?** Because it easily **grabs people's attention** and it **looks cool**(*duh!obviously!*).

The best dimensions for the banner is **1280x650px**. You could also use this for social preview of your repo.

I personally use [**Canva**](https://www.canva.com/) for creating the banner images. All the basic stuff is **free**(*you won't need the pro version in most cases*).

There are endless badges that you could use in your projects. And they do depend on the project. Some of the ones that I commonly use in every projects are given below. 

I use [**Shields IO**](https://shields.io/) for making badges. It is a simple and easy to use tool that you can use for almost all your badge cravings. -->

<!-- Some badges that you could use -->

<!-- ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
: This badge shows the version of the current release.

![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
: I think it is self-explanatory. This gives people an idea about how the project is being maintained.

![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
: This is a dynamic badge from [**Shields IO**](https://shields.io/) that tracks issues in your project and gets updated automatically. It gives the user an idea about the issues and they can just click the badge to view the issues.

![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
: This is also a dynamic badge that tracks pull requests. This notifies the maintainers of the project when a new pull request comes.

![GitHub All Releases](https://img.shields.io/github/downloads/navendu-pottekkat/awesome-readme/total): If you are not like me and your project gets a lot of downloads(*I envy you*) then you should have a badge that shows the number of downloads! This lets others know how **Awesome** your project is and is worth contributing to.

![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)
: This shows what kind of open-source license your project uses. This is good idea as it lets people know how they can use your project for themselves.

![Tweet](https://img.shields.io/twitter/url?style=flat-square&logo=twitter&url=https%3A%2F%2Fnavendu.me%2Fnsfw-filter%2Findex.html): This is not essential but it is a cool way to let others know about your project! Clicking this button automatically opens twitter and writes a tweet about your project and link to it. All the user has to do is to click tweet. Isn't that neat? -->

# Demo-Preview

<!-- Add a demo for your project -->

<!-- After you have written about your project, it is a good idea to have a demo/preview(**video/gif/screenshots** are good options) of your project so that people can know what to expect in your project. You could also add the demo in the previous section with the product description.

Here is a random GIF as a placeholder.

![Random GIF](https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif) -->

# Table of contents

<!-- After you have introduced your project, it is a good idea to add a **Table of contents** or **TOC** as **cool** people say it. This would make it easier for people to navigate through your README and find exactly what they are looking for.

Here is a sample TOC(*wow! such cool!*) that is actually the TOC for this README. -->

- [Project Title](#project-title)
- [Demo-Preview](#demo-preview)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contribute](#contribute)
    - [Sponsor](#sponsor)
    - [Adding new features or fixing bugs](#adding-new-features-or-fixing-bugs)
- [License](#license)
- [Footer](#footer)

# Installation
[(Back to top)](#table-of-contents)

<!-- *You might have noticed the **Back to top** button(if not, please notice, it's right there!). This is a good idea because it makes your README **easy to navigate.*** 

The first one should be how to install(how to generally use your project or set-up for editing in their machine).

This should give the users a concrete idea with instructions on how they can use your project repo with all the steps.

Following this steps, **they should be able to run this in their device.**

A method I use is after completing the README, I go through the instructions from scratch and check if it is working. -->

<!-- Here is a sample instruction:

To use this project, first clone the repo on your device using the command below:

```git init```

```git clone https://github.com/navendu-pottekkat/nsfw-filter.git``` -->

# Usage
[(Back to top)](#table-of-contents)

<!-- This is optional and it is used to give the user info on how to use the project after installation. This could be added in the Installation section also. -->

# Code Documentation
[(Back to top)](#table-of-contents)

The backend of our smart bag application, is coded in Python using the library Flask.
The datasets used in the recommendation system consists of dummy data we created, with an aim to make it seem as real (and random) as possible. The datasets are as followed:
1) orderHistory.csv - Contains the order history of the entire user base of the application. It has the attributes of Order ID, User ID, Product Name, Product ID, Product Brand, and its price. 
2) products.csv - This dataset contains the information about each and every product available on the web app, including its PID, Name, Brand and Price.
3) browseHistory.csv - This dataset contains the browser history of the entire use base, containing a User ID, the browse query, and the date.

A high level overview of the algorithm used would be as follows:
1) A set of attributes would be used to pre compute similarity amongst different products. These include: 
    * The price of the products
    * The name of the products
    * The brand of the products
2) A user logging in would have an ID mapped, which would be used to fetch his specific Order History and Browse History. 
3) Using the Order History, the data of that user is used to create another set of attributes. The new attributes include:
    * The date of ordering of his previous items
    * The brand preference of the user 
4) All of this data is clubbed together into a (Products X Attributes) Matrix. We then find its Correlation Matrix.
5) Using the correlation matrix, we get information about which product is the most linked to another set of products.
6) Now, using the browse queries of the user, we find possible products using a simple application of Levenshtein Distance (or edit distance). We create a list of possible products the user was trying to search
7) Now, we have both the tools required to get the final recommendations, the possible products and the correlation matrix of the products.
8) The algorithm then finds the products most related to the products present in the Possible Products list, and a randomizer is used incase of a large quantity of products.
9) This would be the final recommmendations provided for the user, which are then relayed back to our front end.

## Attributes
All the numeric attributes used were standardized in a range of 0-1, so that none of the attribute dominates over others. Apart from that boolean values were also used.

### Pre Computed Attributes
#### **Price Attribute**
* The products.csv dataset has the information related to all the products, including their prices. 
* The intution behind why we are using the price as a relation attribute, is that in real life scenarios, if a user is buying products in a specific price range, there is a high chance he would keep buying items from similar price ranges.
* So, a precomputation was done regarding the standardization of the price in the range of 0-1. The formula used is: 
>  standardized_price = (maxPrice - product_price)/(maxPrice - minPrice) 

#### **Name of the Product Attribute**
* This attribute basically relates the products with each other depending on the similarity in their names. 
* For this, we used a random string, and calculated the Levenshtein Distance of each product name with this random string. Now, if there are two products with similar brands, they would be giving a similar value, and thus would be deemed as related.
* So, a precomputation was done regarding the standardization of the similarity in the range of 0-1. The formula used is: 
>  standardized_name = (maxSimilarity - product_similarity)/(maxSimilarity - minSimilarity) 

#### **Brand of the Product Attribute**
* This attribute basically relates the products with each other depending on the similarity in their brands. 
* For this, we used a random string, and calculated the Levenshtein Distance of each product Brand with this random string. Now, if there are two products with similar brands, they would be giving a similar value, and thus would be deemed as related.
* So, a precomputation was done regarding the standardization of the similarity in the range of 0-1. The formula used is: 
>  standardized_brand = (maxSimilarity - product_similarity)/(maxSimilarity - minSimilarity) 

### User Specific Attributes
#### **Brand Preference of User Attribute**
* The orderHistory.csv dataset has the information related to all the previous orders of different users. We fetch the data for a specific userId using a simple API call to our backend.
* This attribute is a very important one in deciding the recommendations, as the user would obviously love to be recommended of items of brands which he has previously ordered, considering a specific trust he has on that brand. 
* For using this attribute, first of all, we extract all the brands bought by a user in his order history, and store them in a **set**. Now, we mark all the products of that brand a boolean 1, and rest of the products a boolean 0.
* This automatically is standardized in the desired range, and also is powerful enough to affect the recommendations.


#### **Date of products ordered in previous orders Attribute**
* The orderHistory.csv dataset has the information related to all the previous order histories of different users. We fetch the data for a specific userId using a simple API call to our backend.
* The intution behind why we are using the price as a relation attribute, is that in real life scenarios, especially in grocery related shopping experiences, there is an increased tendency for repetitve orders. Thus, we gave a certain weight to previous orders of the user according to the date they were ordered on, the most recent one being given the highest.
* We calculated the difference of dates with respect to the most recent order of the user. So, if order 1 is the most recent order, it would be given a weight of 1, and the rest of the differences are calculated w.r.t this date. These are then standardized into the range of 0-1 using the same standardization formulas used above


# Functions used in the backend.
Below is a detailed list of the functions used, giving a brief information of what it does, including the parameters they use and their return types.


        
<!-- This is the place where you give instructions to developers on how to modify the code.

You could give **instructions in depth** of **how the code works** and how everything is put together.

You could also give specific instructions to how they can setup their development environment.

Ideally, you should keep the README simple. If you need to add more complex explanations, use a wiki. Check out [this wiki](https://github.com/navendu-pottekkat/nsfw-filter/wiki) for inspiration. -->
# Further Optimization Plans
Some optimizations which we have in mind that can be made for the sake of scalability: 
1) Currently, the technique in which data is being stored is a kind of an ad-hoc technique. Once the application starts scaling, we can make a better organized database with the orderHistory and browserHistory being mapped to each user, instead of a large csv file. This would be a space-time tradeoff, but would improve the algorithm draastically as we would have O(1) time retreival of data for a specific user.

# Contribute
[(Back to top)](#table-of-contents)

<!-- This is where you can let people know how they can **contribute** to your project. Some of the ways are given below.

Also this shows how you can add subsections within a section. -->

### Sponsor
[(Back to top)](#table-of-contents)

<!-- Your project is gaining traction and it is being used by thousands of people(***with this README there will be even more***). Now it would be a good time to look for people or organisations to sponsor your project. This could be because you are not generating any revenue from your project and you require money for keeping the project alive.

You could add how people can sponsor your project in this section. Add your patreon or GitHub sponsor link here for easy access.

A good idea is to also display the sponsors with their organisation logos or badges to show them your love!(*Someday I will get a sponsor and I can show my love*) -->

### Adding new features or fixing bugs
[(Back to top)](#table-of-contents)

<!-- This is to give people an idea how they can raise issues or feature requests in your projects. 

You could also give guidelines for submitting and issue or a pull request to your project.

Personally and by standard, you should use a [issue template](https://github.com/navendu-pottekkat/nsfw-filter/blob/master/ISSUE_TEMPLATE.md) and a [pull request template](https://github.com/navendu-pottekkat/nsfw-filter/blob/master/PULL_REQ_TEMPLATE.md)(click for examples) so that when a user opens a new issue they could easily format it as per your project guidelines.

You could also add contact details for people to get in touch with you regarding your project. -->

# License
[(Back to top)](#table-of-contents)

<!-- Adding the license to README is a good practice so that people can easily refer to it.

Make sure you have added a LICENSE file in your project folder. **Shortcut:** Click add new file in your root of your repo in GitHub > Set file name to LICENSE > GitHub shows LICENSE templates > Choose the one that best suits your project!

I personally add the name of the license and provide a link to it like below. -->

[GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)

# Footer
[(Back to top)](#table-of-contents)

<!-- Let's also add a footer because I love footers and also you **can** use this to convey important info.

Let's make it an image because by now you have realised that multimedia in images == cool(*please notice the subtle programming joke). -->

<!-- Add the footer here -->

<!-- ![Footer](https://github.com/navendu-pottekkat/awesome-readme/blob/master/fooooooter.png) -->
