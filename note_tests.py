from note import Note
import unittest
import numpy as np

myNote = Note('g')

class Note_Tests(unittest.TestCase):

    def test_note(self):
        self.assertEqual(myNote.index, 7)
        self.assertEqual(myNote.octave, 4)
        self.assertAlmostEqual(myNote.frequency(), 392.00, places=2)

    def test_transpose(self):
        myNote.transpose(2) # new note: a4
        self.assertAlmostEqual(myNote.frequency(), 440.00)

        myNote.transpose(24) # new note: a6
        self.assertEqual(myNote.octave, 6)
        self.assertAlmostEqual(myNote.frequency(), 1760.00)

unittest.main()
