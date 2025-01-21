
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalLawModule import PhysicalLaw







class FaradaysFirstLawOfElectrolysis(PhysicalLaw):
    """
    Class representing the `FaradaysFirstLawOfElectrolysis` entity, which inherits from:
    - PhysicalLaw

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1152ae6b_8b57_4d99_912e_40c6a29342fb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FaradaysFirstLawOfElectrolysis'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FaradaysFirstLawOfElectrolysis(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1152ae6b_8b57_4d99_912e_40c6a29342fb',
    
    class_name='FaradaysFirstLawOfElectrolysis',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1152ae6b_8b57_4d99_912e_40c6a29342fb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FaradaysFirstLawOfElectrolysis',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    