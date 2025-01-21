
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity



from .MechanicalQuantityModule import MechanicalQuantity







class CoefficientOfFriction(ISQDimensionlessQuantity, MechanicalQuantity):
    """
    Class representing the `CoefficientOfFriction` entity, which inherits from:
    - ISQDimensionlessQuantity, MechanicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a18a3e9b_7e3d_44bf_9640_c8634e770ba8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CoefficientOfFriction'`
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CoefficientOfFriction(
    
    class_iri='https://w3id.org/emmo#EMMO_a18a3e9b_7e3d_44bf_9640_c8634e770ba8',
    
    class_name='CoefficientOfFriction',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a18a3e9b_7e3d_44bf_9640_c8634e770ba8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CoefficientOfFriction',
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
    

    
    

    

    