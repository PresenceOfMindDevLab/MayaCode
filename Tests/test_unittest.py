import unittest

import Core.Parser as pars

class TestParser(unittest.TestCase):
    
    def testParserReadTrigger(self):
        self.assertEqual(pars.ReadTrigger("dead"), ("dead", "equals"))
        self.assertEqual(pars.ReadTrigger("maya"), ("maya", "equals"))
    
    def testParserReadReplySimple(self):
        self.assertEqual(pars.ReadReply("*pat*"), ("*pat*", "simple_interactions"))
    
    def testParserRedReplyUserInt(self):
        self.assertEqual(pars.ReadReply("maya kill him"), ("kill him", "user_interactions"))