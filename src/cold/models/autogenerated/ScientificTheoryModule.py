
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObservedModule import Observed



from .ObjectiveModule import Objective



from .TheoryModule import Theory







class ScientificTheory(Observed, Objective, Theory):
    """
    Class representing the `ScientificTheory` entity, which inherits from:
    - Observed, Objective, Theory

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_937757d3_ed79_4ae3_9513_3b135e58a6a1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ScientificTheory'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ScientificTheory(
    
    class_iri='https://w3id.org/emmo#EMMO_937757d3_ed79_4ae3_9513_3b135e58a6a1',
    
    class_name='ScientificTheory',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_937757d3_ed79_4ae3_9513_3b135e58a6a1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ScientificTheory',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    