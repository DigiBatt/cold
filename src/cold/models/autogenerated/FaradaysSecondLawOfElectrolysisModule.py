
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalLawModule import PhysicalLaw







class FaradaysSecondLawOfElectrolysis(PhysicalLaw):
    """
    Class representing the `FaradaysSecondLawOfElectrolysis` entity, which inherits from:
    - PhysicalLaw

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_60c5b2e5_164a_4ce6_8409_f386f5e50c03'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FaradaysSecondLawOfElectrolysis'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FaradaysSecondLawOfElectrolysis(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_60c5b2e5_164a_4ce6_8409_f386f5e50c03',
    
    class_name='FaradaysSecondLawOfElectrolysis',
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_60c5b2e5_164a_4ce6_8409_f386f5e50c03',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FaradaysSecondLawOfElectrolysis',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    