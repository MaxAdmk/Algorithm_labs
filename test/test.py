import unittest
import filecmp
import os

from src.topological_sort import topological_sort_dfs, Graph


class TestTopologicalSortDFS(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_topological_sort_dfs(self):
        input_data = [
            "visa foreignpassport",
            "visa hotel",
            "visa bankstatement",
            "bankstatement nationalpassport",
            "hotel creditcard",
            "creditcard nationalpassport",
            "nationalpassport birthcertificate",
            "foreignpassport nationalpassport",
            "foreignpassport militarycertificate",
            "militarycertificate nationalpassport"
        ]
        for line in input_data:
            first_word, second_word = line.strip().split()
            self.graph.add_vertex(first_word)
            self.graph.add_vertex(second_word)
            self.graph.add_edge(first_word, second_word)

        sorted_vertices = topological_sort_dfs(self.graph)

        sorted_vertices.reverse()

        expected_output = [
            'birthcertificate',
            'nationalpassport',
            'militarycertificate',
            'foreignpassport',
            'creditcard',
            'hotel',
            'bankstatement',
            'visa'
        ]

        sorted_vertices_sorted = sorted(sorted_vertices)
        expected_output_sorted = sorted(expected_output)

        self.assertEqual(sorted_vertices_sorted, expected_output_sorted)

        actual_output_file = "actual_output.txt"
        with open(actual_output_file, "w", newline=os.linesep) as f:
            for vertex in sorted_vertices:
                f.write(vertex + "\n")

        expected_output_file = "expected_output.txt"
        with open(expected_output_file, "w", newline=os.linesep) as f:
            for vertex in expected_output:
                f.write(vertex + "\n")

        self.assertTrue(filecmp.cmp(expected_output_file, actual_output_file, shallow=False))
        os.remove(expected_output_file)
        os.remove(actual_output_file)


if __name__ == '__main__':
    unittest.main()
