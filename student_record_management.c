#include <math.h>
#include <stdio.h>
#include <stdlib.h>

struct Node {
  int id;
  float gpa;
  struct Node *prev;
  struct Node *next;
};

struct Node *deleteHead(struct Node *head) {
  // Code to delete head from the dll and return new head(4.2)
  if (head == NULL || head->next == NULL) {
      return head;
  }
  head = head->next;
  head->prev = NULL;
  return head;
}

struct Node *removeDuplicates(struct Node *head, int id) {
  // Code to delete all occurences of the record id and
  // keep only the oldest record with id=id and return new head(4.3)
  if (head == NULL || head->next == NULL) {
      return head;
  }
  struct Node* current = head;
  int counter = 0;
  while (current != NULL) {
    if (current->id == id) {
      counter++;
      if (counter > 1) { 
        if (current->next != NULL) {
          current->next->prev = current->prev;
        }
        if (current->prev != NULL) {
          current->prev->next = current->next;
        }
      }
    }
    current = current->next; 
  }
  return head;
}

// Code to reverse and dll return new head(4.4)
struct Node *reverse(struct Node *head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }

    struct Node *current = head;
    struct Node *prev = NULL;

    while (current != NULL) {
        struct Node *next = current->next;
        current->next = prev;
        current->prev = next;
        prev = current;
        current = next;
    }

    return prev;
}

struct Node *rotateByKplaces(struct Node *head, int k) {
   // Code to rotate the dll by k places to the right and return new head(4.5)
  if (head == NULL || head->next == NULL) {
    return head;
  }

  struct Node *current = head;
  struct Node *tail = head;
  int count = 1;
  while (tail->next != NULL) {
    count++;
    tail = tail->next;
  }
  tail->next = head;
  head->prev = tail;

  int rotateCount = count - (k % count);

  for (int i = 0; i < rotateCount; i++) {
    current = current->next;
  }

  head = current;
  head->prev->next = NULL;
  head->prev = NULL;

  return head;
}

struct Node *createSortedList(struct Node *head) {
  // Code to create a new dll sorted by gpa (4.6)
  if (head == NULL || head->next == NULL) {
      return head;
  }

  struct Node *current = head;
  struct Node *sorted_head = NULL;
  struct Node *temp = NULL;

  while (current != NULL) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->id = current->id;
    newNode->gpa = current->gpa;

    if (sorted_head == NULL) {
      sorted_head = newNode;
      sorted_head->prev = NULL;
      sorted_head->next = NULL;
    } else {
      temp = sorted_head;
      while (temp != NULL) {
        if (newNode->gpa < temp->gpa) {
          if (temp->prev == NULL) {
            sorted_head = newNode;
            newNode->prev = NULL;
            newNode->next = temp;
            temp->prev = newNode;
          } else {
            temp->prev->next = newNode;
            newNode->prev = temp->prev;
            newNode->next = temp;
            temp->prev = newNode;
          }
          break;
        } else if (temp->next == NULL) {
          temp->next = newNode;
          newNode->prev = temp;
          newNode->next = NULL;
          break;
        }
        temp = temp->next;
      }
    }
    current = current->next;
  }

  return sorted_head;
}

int main() {
  struct Node *head;
  struct Node *sorted_head;
  head = (struct Node *)malloc(sizeof(struct Node));
  sorted_head = (struct Node *)malloc(sizeof(struct Node));
  head->next = NULL;
  head->prev = NULL;
  // code to take n, k, duplicate_id as input
  int n, k, duplicate_id;
  scanf("%d %d %d", &n, &k, &duplicate_id);
  // code to take input n records input and build a dll(4.1)
  // ...
  struct Node *end = NULL;
  for (int i = 0; i < n; i++) {
    struct Node *current = (struct Node *)malloc(sizeof(struct Node));
    scanf("%d %f", &current->id, &current->gpa);
    current->prev = end;
    current->next = NULL;

    if (end != NULL) {
      end->next = current;
    } else {
      head = current;
    }
    end = current;
  }
   // head updated
  head = deleteHead(head);
  head = removeDuplicates(head, duplicate_id);
  head = reverse(head);
  head = rotateByKplaces(head, k);
  sorted_head = createSortedList(head);

  // Do not modify the code below
  struct Node *curr = head;
  struct Node *tail = head;
  // print head
  while (curr != NULL) {
    printf("%d,%.1f->", curr->id, curr->gpa);
    tail = curr;
    curr = curr->next;
  }
  printf("\n");
  // print head in reverse order
  while (tail != NULL) {
    printf("%d,%.1f->", tail->id, tail->gpa);
    tail = tail->prev;
  }
  printf("\n");

  curr = sorted_head;
  tail = curr;
  // print sorted_head in reverse order
  while (curr != NULL) {
    printf("%d,%.1f->", curr->id, curr->gpa);
    tail = curr;
    curr = curr->next;
  }
  printf("\n");
  // print sorted_head in reverse order
  while (tail != NULL) {
    printf("%d,%.1f->", tail->id, tail->gpa);
    tail = tail->prev;
  }
  printf("\n");

  return 0;
}
