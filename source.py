#!/usr/bin/env python2.7

import dataSource


def execute():
     popularArticles()

    print "\n"
    popularAurthors()

    print "\n"
    daysOfErrors()


def popularArticles():
    print "1. What are the most popular three articles of all time?\n"
    rows = dataSource.articles()
    for row in rows:
        print "%s - %d views" % (row[0], row[1])


def popularAuthors():
    print "2. Who are the most popular article authors of all time?\n"
    rows = dataSource.authors()
    for row in rows:
        print "%s - %d views" % (row[0], row[1])


def daysOfError():
    print "3. On which days did more than 1% of requests lead to errors?\n"
    rows = dataSource.errors()
    for row in rows:
        print "%s - %s errors" % (row[0], row[1])

execute()