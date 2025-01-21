
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity







class ActivityOfSolvent(PhysioChemicalQuantity, ISQDimensionlessQuantity):
    """
    Class representing the `ActivityOfSolvent` entity, which inherits from:
    - PhysioChemicalQuantity, ISQDimensionlessQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2ed364b1_affe_4711_a83f_74bfd57b94ad'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActivityOfSolvent'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ActivityOfSolvent(
    
    class_iri='https://w3id.org/emmo#EMMO_2ed364b1_affe_4711_a83f_74bfd57b94ad',
    
    class_name='ActivityOfSolvent',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2ed364b1_affe_4711_a83f_74bfd57b94ad',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActivityOfSolvent',
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
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    