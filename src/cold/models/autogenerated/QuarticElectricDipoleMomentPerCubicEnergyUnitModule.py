
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class QuarticElectricDipoleMomentPerCubicEnergyUnit(SIDimensionalUnit):
    """
    Class representing the `QuarticElectricDipoleMomentPerCubicEnergyUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c0487653_66e8_454e_bb11_e50167e412e4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'QuarticElectricDipoleMomentPerCubicEnergyUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = QuarticElectricDipoleMomentPerCubicEnergyUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_c0487653_66e8_454e_bb11_e50167e412e4',
    
    class_name='QuarticElectricDipoleMomentPerCubicEnergyUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c0487653_66e8_454e_bb11_e50167e412e4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'QuarticElectricDipoleMomentPerCubicEnergyUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    