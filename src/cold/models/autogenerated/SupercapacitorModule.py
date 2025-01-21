
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalDeviceModule import ElectrochemicalDevice







class Supercapacitor(ElectrochemicalDevice):
    """
    Class representing the `Supercapacitor` entity, which inherits from:
    - ElectrochemicalDevice

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dc6abae7_39b0_4d22_b52e_14d088a4bd5f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Supercapacitor'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Supercapacitor(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dc6abae7_39b0_4d22_b52e_14d088a4bd5f',
    
    class_name='Supercapacitor',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dc6abae7_39b0_4d22_b52e_14d088a4bd5f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Supercapacitor',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    