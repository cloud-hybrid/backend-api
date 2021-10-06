- [ ] Create a `Mongo.Collections.Lanes` Package
    - [ ] `/Mongo/Collections/Lanes` Directory
    - [ ] `/Mongo/Collections/Lanes/__init__.py` File
    - [ ] `/Mongo/Collections/Lanes/CRUD.py` File
- [ ] Create a `Mongo.Interfaces.Lane` Module
    - [ ] `/Mongo/Interfaces/Lane.py` File
- [ ] Create a `Mongo.Schemas.Lane` Module
    - [ ] `/Mongo/Schemas/Lane.py` File

## Requirements ##

- Lane Schema should have a property `Label` which describes the name of the lane
- Lane Schema should have a property `Tasks` which is an array of associated Task Items
    - Only "FK"'s or "_ids"/"ID" are stored
- Lane Schema should have a property `Board` which is a "FK" association to a Parent Board
- Lane Schema should have a property [`Meta`](https://devhints.io/html-meta)
    - Reference: https://devhints.io/html-meta
    - Reference: https://developer.twitter.com/en/docs/twitter-for-websites/cards/guides/getting-started
    - The `Meta` Type should be a Type of two sub-types:
         - `Summary` Type
             - `Twitter` Type
                 - `Key: String = "Name"`
                 - `Card: String = Field(..., alias = "Summary" description = "Summary ...")`
                 - `Site: String = Field(default = "@cloud-technology", alias = "Site" description = "...")`
                 - `Creator: String = Field(default = "@Null-Byte", alias = "Creator" description = "...")`
             - `Open` Type
                 - `Key: String = "Property"`
                 - `URL: URL = Field(..., alias = "URL" description = "...")`
                 - `Title: String = Field(..., alias = "Title" description = "...")`
                 - `Description: String = Field(..., alias = "Description" description = "...", max = 1000)`
                 - `Image: Upload = Field(..., alias = "Upload" description = "...")`
                     - `Upload` Type
                         - `ID: ...`
                         - `Canonical: String`
                         - `File-Name: String`
                         - `Content: URL`
- Lane API should have a `@staticmethod` for Generating HTML `<Head>` metadata from an argument of type `Mongo.Schemas.Lane.Summary` (as previously mentioned):

```html
<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="@nytimesbits" />
<meta name="twitter:creator" content="@nickbilton" />
<meta property="og:url" content="http://bits.blogs.nytimes.com/2011/12/08/a-twitter-for-my-sister/" />
<meta property="og:title" content="A Twitter for My Sister" />
<meta property="og:description" content="In the early days, Twitter grew so quickly that it was almost impossible to add new features because engineers spent their time trying to keep the rocket ship from stalling." />
<meta property="og:image" content="http://graphics8.nytimes.com/images/2011/12/08/technology/bits-newtwitter/bits-newtwitter-tmagArticle.jpg" />
```
