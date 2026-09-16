from __future__ import annotations

class Study:
    def __init__(self, mtk_nr: int, first_name: str, last_name: str):
        self.mtk_nr = mtk_nr
        self.first_name = first_name
        self.last_name = last_name

    def mtk_nr(self) -> int:
        return self.mtk_nr

    def first_name(self) -> str:
        return self.first_name

    def last_name(self) -> str:
        return self.last_name

    def __str__(self) -> str:
        return "[" + str(self.mtk_nr) + " " + self.first_name + " " + self.last_name + "]"


class BinaryTree:
    def __init__(self, study):
        self.study = study
        self.left = None
        self.right = None

    def study(self) -> Study:
        return self.study

    def left(self) -> BinaryTree:
        return self.left

    def right(self) -> BinaryTree:
        return self.right

    def append(self, study: Study):
        current_tree: BinaryTree = self
        while current_tree is not None:
            if current_tree.study.mtk_nr > study.mtk_nr:
                if current_tree.left is None:
                    current_tree.left = BinaryTree(study)
                    return
                else:
                    current_tree = current_tree.left
            else:
                if current_tree.right is None:
                    current_tree.right = BinaryTree(study)
                    return
                else:
                    current_tree = current_tree.right

    def contains(self, study: Study) -> bool:
        if self.study.mtk_nr == study.mtk_nr:
            return True
        if study.mtk_nr < self.study.mtk_nr:
            return self.left.contains(study)
        if study.mtk_nr >= self.study.mtk_nr:
            return self.right.contains(study)
        return False

    def __str__(self):
        return str(self.left) + ", " + str(self.study) + ", " + str(self.right)

if __name__ == '__main__':
    study1 = Study(1, "yannick", "weber")
    study2 = Study(2, "max", "mustermann")
    study3 = Study(3, "must", "maxermann")

    myTree = BinaryTree(study2)
    print(myTree)

    myTree.append(study1)
    print(myTree)

    myTree.append(study3)
    print(myTree)

