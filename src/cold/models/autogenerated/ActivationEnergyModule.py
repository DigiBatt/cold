
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MolarEnergyModule import MolarEnergy







class ActivationEnergy(MolarEnergy):
    """
    Class representing the `ActivationEnergy` entity, which inherits from:
    - MolarEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d7f8cab9_b035_4ecd_be63_292672572526'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActivationEnergy'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ActivationEnergy(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d7f8cab9_b035_4ecd_be63_292672572526',
    
    class_name='ActivationEnergy',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d7f8cab9_b035_4ecd_be63_292672572526',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActivationEnergy',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    