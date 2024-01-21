import graphene
from graphene_django import DjangoObjectType
from .models import Publisher, Author, Book

class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    publishers = graphene.List(PublisherType)
    authors = graphene.List(AuthorType)
    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID())
    author = graphene.Field(AuthorType, id=graphene.ID())
    publisher = graphene.Field(PublisherType, id=graphene.ID())

    def resolve_publisher(self, info, id):
        return Publisher.objects.get(pk=id)

    def resolve_author(self, info, id):
        return Author.objects.get(pk=id)

    def resolve_book(self, info, id):
        return Book.objects.get(pk=id)

    def resolve_publishers(self, info):
        return Publisher.objects.all()

    def resolve_authors(self, info):
        return Author.objects.all()

    def resolve_books(self, info):
        return Book.objects.all()


class CreatePublisher(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address = graphene.String(required=True)

    publisher = graphene.Field(PublisherType)

    def mutate(self, info, name, address):
        publisher = Publisher(name=name, address=address)
        publisher.save()
        return CreatePublisher(publisher=publisher)


class UpdatePublisher(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        address = graphene.String()

    publisher = graphene.Field(PublisherType)

    def mutate(self, info, id, **kwargs):
        publisher = Publisher.objects.get(pk=id)
        for key, value in kwargs.items():
            setattr(publisher, key, value)
        publisher.save()
        return UpdatePublisher(publisher=publisher)


class DeletePublisher(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    publisher_id = graphene.ID()

    def mutate(self, info, id):
        publisher = Publisher.objects.get(pk=id)
        publisher.delete()
        return DeletePublisher(publisher_id=id)


class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        bio = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    def mutate(self, info, name, bio):
        author = Author(name=name, bio=bio)
        author.save()
        return CreateAuthor(author=author)


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        bio = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, id, **kwargs):
        author = Author.objects.get(pk=id)
        for key, value in kwargs.items():
            setattr(author, key, value)
        author.save()
        return UpdateAuthor(author=author)


class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    author_id = graphene.ID()

    def mutate(self, info, id):
        author = Author.objects.get(pk=id)
        author.delete()
        return DeleteAuthor(author_id=id)


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        published_date = graphene.String(required=True)
        author_id = graphene.ID(required=True)
        publisher_id = graphene.ID(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, title, published_date, author_id, publisher_id):
        author = Author.objects.get(pk=author_id)
        publisher = Publisher.objects.get(pk=publisher_id)
        book = Book(title=title, published_date=published_date, author=author, publisher=publisher)
        book.save()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        published_date = graphene.String()
        author_id = graphene.ID()
        publisher_id = graphene.ID()

    book = graphene.Field(BookType)

    def mutate(self, info, id, **kwargs):
        book = Book.objects.get(pk=id)
        for key, value in kwargs.items():
            setattr(book, key, value)
        book.save()
        return UpdateBook(book=book)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    book_id = graphene.ID()

    def mutate(self, info, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return DeleteBook(book_id=id)


class Mutation(graphene.ObjectType):
    create_publisher = CreatePublisher.Field()
    update_publisher = UpdatePublisher.Field()
    delete_publisher = DeletePublisher.Field()
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)