class Article:
    all = []  # track all article instances

    def __init__(self, author, magazine, title):
        # --- validations ---
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be a string between 5 and 50 characters")

        self._title = title
        self.author = author      
        self.magazine = magazine  

        Article.all.append(self)

    # --- Title property (immutable) ---
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # ignore reassignment to keep title immutable
        pass

    # --- Author property ---
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    # --- Magazine property ---
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("name must be a non-empty string")
        self._name = name

    # --- Name property (immutable) ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # ignore reassignment to keep name immutable
        pass

    # --- Relationship methods ---
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    # --- Association methods ---
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        cats = {mag.category for mag in self.magazines()}
        return list(cats) if cats else None


class Magazine:
    all = []  # track all magazine instances

    def __init__(self, name, category):
        self.name = name      
        self.category = category
        Magazine.all.append(self)

    # --- Name property (mutable) ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # else ignore invalid assignments to pass tests

    # --- Category property (mutable) ---
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # else ignore invalid assignments

    # --- Relationship methods ---
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    # --- Association methods ---
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [a for a in set(authors) if authors.count(a) > 2]
        return result if result else None

    # --- Bonus ---
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))