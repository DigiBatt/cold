
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectiveModule import Objective



from .TheoryModule import Theory



from .EstimatedModule import Estimated







class Hypothesis(Objective, Theory, Estimated):
    """
    Class representing the `Hypothesis` entity, which inherits from:
    - Objective, Theory, Estimated

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e7cbc129_0d05_41a2_851a_10b198cd7ca2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Hypothesis'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Hypothesis(
    
    class_iri='https://w3id.org/emmo#EMMO_e7cbc129_0d05_41a2_851a_10b198cd7ca2',
    
    class_name='Hypothesis',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e7cbc129_0d05_41a2_851a_10b198cd7ca2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Hypothesis',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    