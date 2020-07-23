# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Any, AsyncIterable, Awaitable, Callable, Iterable, Sequence, Tuple

from google.analytics.admin_v1alpha.types import analytics_admin
from google.analytics.admin_v1alpha.types import resources


class ListAccountsPager:
    """A pager for iterating through ``list_accounts`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListAccountsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``accounts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAccounts`` requests and continue to iterate
    through the ``accounts`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListAccountsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListAccountsResponse],
        request: analytics_admin.ListAccountsRequest,
        response: analytics_admin.ListAccountsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListAccountsRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListAccountsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListAccountsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[analytics_admin.ListAccountsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[resources.Account]:
        for page in self.pages:
            yield from page.accounts

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccountsAsyncPager:
    """A pager for iterating through ``list_accounts`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListAccountsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``accounts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAccounts`` requests and continue to iterate
    through the ``accounts`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListAccountsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListAccountsResponse]],
        request: analytics_admin.ListAccountsRequest,
        response: analytics_admin.ListAccountsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListAccountsRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListAccountsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListAccountsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[analytics_admin.ListAccountsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[resources.Account]:
        async def async_generator():
            async for page in self.pages:
                for response in page.accounts:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPropertiesPager:
    """A pager for iterating through ``list_properties`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListPropertiesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``properties`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProperties`` requests and continue to iterate
    through the ``properties`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListPropertiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListPropertiesResponse],
        request: analytics_admin.ListPropertiesRequest,
        response: analytics_admin.ListPropertiesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListPropertiesRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListPropertiesResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListPropertiesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[analytics_admin.ListPropertiesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[resources.Property]:
        for page in self.pages:
            yield from page.properties

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPropertiesAsyncPager:
    """A pager for iterating through ``list_properties`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListPropertiesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``properties`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProperties`` requests and continue to iterate
    through the ``properties`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListPropertiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListPropertiesResponse]],
        request: analytics_admin.ListPropertiesRequest,
        response: analytics_admin.ListPropertiesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListPropertiesRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListPropertiesResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListPropertiesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[analytics_admin.ListPropertiesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[resources.Property]:
        async def async_generator():
            async for page in self.pages:
                for response in page.properties:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserLinksPager:
    """A pager for iterating through ``list_user_links`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListUserLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``user_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUserLinks`` requests and continue to iterate
    through the ``user_links`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListUserLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListUserLinksResponse],
        request: analytics_admin.ListUserLinksRequest,
        response: analytics_admin.ListUserLinksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListUserLinksRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListUserLinksResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListUserLinksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[analytics_admin.ListUserLinksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[resources.UserLink]:
        for page in self.pages:
            yield from page.user_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserLinksAsyncPager:
    """A pager for iterating through ``list_user_links`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListUserLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``user_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUserLinks`` requests and continue to iterate
    through the ``user_links`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListUserLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListUserLinksResponse]],
        request: analytics_admin.ListUserLinksRequest,
        response: analytics_admin.ListUserLinksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListUserLinksRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListUserLinksResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListUserLinksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[analytics_admin.ListUserLinksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[resources.UserLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.user_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AuditUserLinksPager:
    """A pager for iterating through ``audit_user_links`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.AuditUserLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``user_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``AuditUserLinks`` requests and continue to iterate
    through the ``user_links`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.AuditUserLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.AuditUserLinksResponse],
        request: analytics_admin.AuditUserLinksRequest,
        response: analytics_admin.AuditUserLinksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.AuditUserLinksRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.AuditUserLinksResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.AuditUserLinksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[analytics_admin.AuditUserLinksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[resources.AuditUserLink]:
        for page in self.pages:
            yield from page.user_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AuditUserLinksAsyncPager:
    """A pager for iterating through ``audit_user_links`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.AuditUserLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``user_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``AuditUserLinks`` requests and continue to iterate
    through the ``user_links`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.AuditUserLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.AuditUserLinksResponse]],
        request: analytics_admin.AuditUserLinksRequest,
        response: analytics_admin.AuditUserLinksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.AuditUserLinksRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.AuditUserLinksResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.AuditUserLinksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[analytics_admin.AuditUserLinksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[resources.AuditUserLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.user_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWebDataStreamsPager:
    """A pager for iterating through ``list_web_data_streams`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListWebDataStreamsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``web_data_streams`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWebDataStreams`` requests and continue to iterate
    through the ``web_data_streams`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListWebDataStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListWebDataStreamsResponse],
        request: analytics_admin.ListWebDataStreamsRequest,
        response: analytics_admin.ListWebDataStreamsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListWebDataStreamsRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListWebDataStreamsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListWebDataStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[analytics_admin.ListWebDataStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[resources.WebDataStream]:
        for page in self.pages:
            yield from page.web_data_streams

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWebDataStreamsAsyncPager:
    """A pager for iterating through ``list_web_data_streams`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListWebDataStreamsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``web_data_streams`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWebDataStreams`` requests and continue to iterate
    through the ``web_data_streams`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListWebDataStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListWebDataStreamsResponse]],
        request: analytics_admin.ListWebDataStreamsRequest,
        response: analytics_admin.ListWebDataStreamsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListWebDataStreamsRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListWebDataStreamsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListWebDataStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[analytics_admin.ListWebDataStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[resources.WebDataStream]:
        async def async_generator():
            async for page in self.pages:
                for response in page.web_data_streams:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIosAppDataStreamsPager:
    """A pager for iterating through ``list_ios_app_data_streams`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListIosAppDataStreamsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``ios_app_data_streams`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListIosAppDataStreams`` requests and continue to iterate
    through the ``ios_app_data_streams`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListIosAppDataStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListIosAppDataStreamsResponse],
        request: analytics_admin.ListIosAppDataStreamsRequest,
        response: analytics_admin.ListIosAppDataStreamsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListIosAppDataStreamsRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListIosAppDataStreamsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListIosAppDataStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[analytics_admin.ListIosAppDataStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[resources.IosAppDataStream]:
        for page in self.pages:
            yield from page.ios_app_data_streams

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIosAppDataStreamsAsyncPager:
    """A pager for iterating through ``list_ios_app_data_streams`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListIosAppDataStreamsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``ios_app_data_streams`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListIosAppDataStreams`` requests and continue to iterate
    through the ``ios_app_data_streams`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListIosAppDataStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListIosAppDataStreamsResponse]],
        request: analytics_admin.ListIosAppDataStreamsRequest,
        response: analytics_admin.ListIosAppDataStreamsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListIosAppDataStreamsRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListIosAppDataStreamsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListIosAppDataStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterable[analytics_admin.ListIosAppDataStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[resources.IosAppDataStream]:
        async def async_generator():
            async for page in self.pages:
                for response in page.ios_app_data_streams:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAndroidAppDataStreamsPager:
    """A pager for iterating through ``list_android_app_data_streams`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListAndroidAppDataStreamsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``android_app_data_streams`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAndroidAppDataStreams`` requests and continue to iterate
    through the ``android_app_data_streams`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListAndroidAppDataStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListAndroidAppDataStreamsResponse],
        request: analytics_admin.ListAndroidAppDataStreamsRequest,
        response: analytics_admin.ListAndroidAppDataStreamsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListAndroidAppDataStreamsRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListAndroidAppDataStreamsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListAndroidAppDataStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[analytics_admin.ListAndroidAppDataStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[resources.AndroidAppDataStream]:
        for page in self.pages:
            yield from page.android_app_data_streams

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAndroidAppDataStreamsAsyncPager:
    """A pager for iterating through ``list_android_app_data_streams`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListAndroidAppDataStreamsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``android_app_data_streams`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAndroidAppDataStreams`` requests and continue to iterate
    through the ``android_app_data_streams`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListAndroidAppDataStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[analytics_admin.ListAndroidAppDataStreamsResponse]
        ],
        request: analytics_admin.ListAndroidAppDataStreamsRequest,
        response: analytics_admin.ListAndroidAppDataStreamsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListAndroidAppDataStreamsRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListAndroidAppDataStreamsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListAndroidAppDataStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterable[analytics_admin.ListAndroidAppDataStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[resources.AndroidAppDataStream]:
        async def async_generator():
            async for page in self.pages:
                for response in page.android_app_data_streams:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoogleAdsLinksPager:
    """A pager for iterating through ``list_google_ads_links`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListGoogleAdsLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``google_ads_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoogleAdsLinks`` requests and continue to iterate
    through the ``google_ads_links`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListGoogleAdsLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListGoogleAdsLinksResponse],
        request: analytics_admin.ListGoogleAdsLinksRequest,
        response: analytics_admin.ListGoogleAdsLinksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListGoogleAdsLinksRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListGoogleAdsLinksResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListGoogleAdsLinksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[analytics_admin.ListGoogleAdsLinksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[resources.GoogleAdsLink]:
        for page in self.pages:
            yield from page.google_ads_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoogleAdsLinksAsyncPager:
    """A pager for iterating through ``list_google_ads_links`` requests.

    This class thinly wraps an initial
    :class:`~.analytics_admin.ListGoogleAdsLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``google_ads_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoogleAdsLinks`` requests and continue to iterate
    through the ``google_ads_links`` field on the
    corresponding responses.

    All the usual :class:`~.analytics_admin.ListGoogleAdsLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListGoogleAdsLinksResponse]],
        request: analytics_admin.ListGoogleAdsLinksRequest,
        response: analytics_admin.ListGoogleAdsLinksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.analytics_admin.ListGoogleAdsLinksRequest`):
                The initial request object.
            response (:class:`~.analytics_admin.ListGoogleAdsLinksResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = analytics_admin.ListGoogleAdsLinksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[analytics_admin.ListGoogleAdsLinksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[resources.GoogleAdsLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.google_ads_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
