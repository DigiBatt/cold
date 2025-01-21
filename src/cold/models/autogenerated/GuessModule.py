
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SubjectiveModule import Subjective



from .TheoryModule import Theory



from .EstimatedModule import Estimated







class Guess(Subjective, Theory, Estimated):
    """
    Class representing the `Guess` entity, which inherits from:
    - Subjective, Theory, Estimated

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_57b9fd6c_84d6_43f2_8c4f_de6a1ab50aea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Guess'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Guess(
    
    class_iri='https://w3id.org/emmo#EMMO_57b9fd6c_84d6_43f2_8c4f_de6a1ab50aea',
    
    class_name='Guess',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_57b9fd6c_84d6_43f2_8c4f_de6a1ab50aea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Guess',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    