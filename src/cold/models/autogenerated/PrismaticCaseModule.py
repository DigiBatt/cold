
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .CaseModule import Case





from .ConstituentModule import Constituent





class PrismaticCase(Whole, Case):
    """
    Class representing the `PrismaticCase` entity, which inherits from:
    - Whole, Case

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_43cd6e14_dd43_41b5_b5b4_344d53841603'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PrismaticCase'`
        - **Alias**: `class_name`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PrismaticCase(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_43cd6e14_dd43_41b5_b5b4_344d53841603',
    
    class_name='PrismaticCase',
    
    hasConstituent="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_43cd6e14_dd43_41b5_b5b4_344d53841603',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PrismaticCase',
        alias="class_name"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    

    

    