
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturedMaterialModule import ManufacturedMaterial







class OpenCellFoam(ManufacturedMaterial):
    """
    Class representing the `OpenCellFoam` entity, which inherits from:
    - ManufacturedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7cef0da2_8de3_418e_b390_cce9a5d3c129'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OpenCellFoam'`
        - **Alias**: `class_name`
    
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
    obj = OpenCellFoam(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7cef0da2_8de3_418e_b390_cce9a5d3c129',
    
    class_name='OpenCellFoam',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7cef0da2_8de3_418e_b390_cce9a5d3c129',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OpenCellFoam',
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    