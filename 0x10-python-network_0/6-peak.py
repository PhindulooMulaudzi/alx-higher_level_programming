#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    def _find_peak(lo, hi):
        if lo == hi - 1:
            return list_of_integers[lo]

        mid = (lo + hi) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            return _find_peak(lo, mid)
        else:
            return _find_peak(mid + 1, hi)

    if not list_of_integers:
        return None

    return _find_peak(0, len(list_of_integers))
